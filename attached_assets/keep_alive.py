import os
import time
import logging
import threading
from datetime import datetime
from flask import Flask, send_file
import psutil
import requests

app = Flask(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('keep_alive.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def check_bot_process():
    """Check if the bot process is running"""
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            cmdline = ' '.join(proc.info['cmdline'] or [])
            if 'python' in proc.info['name'].lower() and 'bot.py' in cmdline:
                return proc.pid
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return None

def check_bot_health():
    """Check if the bot is responding to Telegram"""
    try:
        bot_token = os.getenv('BOT_TOKEN')
        if not bot_token:
            logger.error("BOT_TOKEN not found in environment variables")
            return False

        response = requests.get(f'https://api.telegram.org/bot{bot_token}/getMe', timeout=10)
        return response.status_code == 200
    except Exception as e:
        logger.error(f"Bot health check failed: {e}")
        return False

@app.route('/')
def home():
    bot_pid = check_bot_process()
    bot_health = check_bot_health() if bot_pid else False
    status = "✅ Bot is running and healthy" if bot_health else "⚠️ Bot is running but not responding" if bot_pid else "❌ Bot is not running"

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    memory_usage = psutil.Process().memory_info().rss / 1024 / 1024  # Convert to MB

    return f"""
    <html>
    <head>
        <meta http-equiv="refresh" content="60">
        <style>
            body {{ 
                background-color: #1a1b26; 
                color: white; 
                font-family: Arial, sans-serif; 
                padding: 20px;
                max-width: 800px;
                margin: 0 auto;
            }}
            .status-card {{
                background-color: #24283b;
                padding: 20px;
                border-radius: 10px;
                margin: 10px 0;
            }}
            .metric {{
                display: flex;
                justify-content: space-between;
                padding: 10px 0;
                border-bottom: 1px solid #414868;
            }}
            .metric:last-child {{
                border-bottom: none;
            }}
        </style>
    </head>
    <body>
        <h1>Bot Status Monitor</h1>
        <div class="status-card">
            <div class="metric">
                <span>Status:</span>
                <span>{status}</span>
            </div>
            <div class="metric">
                <span>Current Time:</span>
                <span>{current_time}</span>
            </div>
            <div class="metric">
                <span>Server Uptime:</span>
                <span>{time.time() - psutil.boot_time():.0f} seconds</span>
            </div>
            <div class="metric">
                <span>Memory Usage:</span>
                <span>{memory_usage:.1f} MB</span>
            </div>
        </div>
    </body>
    </html>
    """

@app.route('/website.zip')
def download_zip():
    try:
        zip_path = os.path.join(os.getcwd(), 'website.zip')
        if os.path.exists(zip_path):
            return send_file(
                zip_path,
                as_attachment=True,
                mimetype='application/zip'
            )
        else:
            logger.error("Zip file not found")
            return "Error: File not found", 404
    except Exception as e:
        logger.error(f"Error serving zip file: {e}")
        return f"Error: {str(e)}", 500

def monitor_bot():
    """Monitor bot health and restart if needed"""
    while True:
        try:
            bot_pid = check_bot_process()
            bot_healthy = check_bot_health() if bot_pid else False

            if not bot_healthy:
                logger.warning("Bot is not healthy, attempting to restart")
                if bot_pid:
                    try:
                        # Kill only the bot process
                        psutil.Process(bot_pid).terminate()
                        time.sleep(2)  # Give it time to terminate gracefully
                    except (psutil.NoSuchProcess, psutil.AccessDenied):
                        pass

                # Start bot process
                logger.info("Starting bot process...")
                os.system('python attached_assets/bot.py &')
                logger.info("Bot restarted")

            time.sleep(60)  # Check every minute
        except Exception as e:
            logger.error(f"Error in monitor thread: {e}")
            time.sleep(60)  # Wait before retry

def run():
    """Run the Flask server"""
    try:
        app.run(host='0.0.0.0', port=8081)
    except Exception as e:
        logger.error(f"Flask server error: {e}")
        time.sleep(10)  # Wait before retry
        run()

def keep_alive():
    """Start the Flask server and monitoring in background threads"""
    server_thread = threading.Thread(target=run)
    monitor_thread = threading.Thread(target=monitor_bot)

    server_thread.daemon = True
    monitor_thread.daemon = True

    server_thread.start()
    monitor_thread.start()

    logger.info("Keep-alive server and monitoring started")

if __name__ == "__main__":
    keep_alive()