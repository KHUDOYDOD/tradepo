# Forex Analysis Telegram Bot

A multi-language Telegram bot for financial market analysis with technical indicators and user management.

## Features

- Multi-language support (Tajik, Russian, Uzbek, Kazakh, English)
- Real-time market analysis
- Technical indicators (RSI, MACD, EMA, Bollinger Bands)
- User authentication system
- Admin panel
- Monitoring system

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/forex-analysis-bot.git
cd forex-analysis-bot
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
# or
.\venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file and add your configuration:
```bash
# Copy example config
cp .env.example .env
# Edit with your values
nano .env
```

## Server Deployment

1. Copy files to server:
```bash
# Create directory
sudo mkdir -p /root/bot
# Copy all files
sudo cp -r * /root/bot/
```

2. Install service:
```bash
# Copy service file
sudo cp telegram-bot.service /etc/systemd/system/
# Reload systemd
sudo systemctl daemon-reload
# Enable service
sudo systemctl enable telegram-bot
# Start service
sudo systemctl start telegram-bot
```

3. Check status:
```bash
# View service status
sudo systemctl status telegram-bot
# View logs
sudo journalctl -u telegram-bot -f
```

4. Monitor via web interface:
```
http://your-server:8081
```

## Management Commands

1. Start bot:
```bash
sudo systemctl start telegram-bot
```

2. Stop bot:
```bash
sudo systemctl stop telegram-bot
```

3. Restart bot:
```bash
sudo systemctl restart telegram-bot
```

4. View logs:
```bash
sudo journalctl -u telegram-bot -f
```

## Monitoring System

The bot includes a built-in monitoring system that:
- Checks bot health every minute
- Automatically restarts if bot crashes
- Provides web interface for status monitoring
- Shows memory usage and uptime statistics

Access monitoring dashboard at:
```
http://your-server:8081
```

## Environment Variables

Required environment variables in `.env`:
- `BOT_TOKEN`: Your Telegram bot token from @BotFather
- `DATABASE_URL`: PostgreSQL database URL
- Other database configuration (see .env.example)