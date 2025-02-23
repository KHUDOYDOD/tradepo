import os
import time
import logging
import threading
from datetime import datetime
from flask import Flask, send_file
import psutil

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
            if 'python' in proc.info['name'].lower() and 'bot.py' in ' '.join(proc.info['cmdline']):
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return False

@app.route('/')
def home():
    bot_status = "✅ Bot is running" if check_bot_process() else "❌ Bot is not running"
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""
    <html>
    <body style="background-color: #1a1b26; color: white; font-family: Arial, sans-serif; padding: 20px;">
        <h1>Bot Status Monitor</h1>
        <p>Current Time: {current_time}</p>
        <p>Status: {bot_status}</p>
        <p>Server Uptime: {time.time() - psutil.boot_time():.0f} seconds</p>
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

def run():
    """Run the Flask server"""
    try:
        app.run(host='0.0.0.0', port=8081)
    except Exception as e:
        logger.error(f"Flask server error: {e}")
        time.sleep(10)  # Wait before retry
        run()

def keep_alive():
    """Start the Flask server in a background thread"""
    server_thread = threading.Thread(target=run)
    server_thread.daemon = True  # Thread will exit when main program exits
    server_thread.start()
    logger.info("Keep-alive server started")

if __name__ == "__main__":
    keep_alive()