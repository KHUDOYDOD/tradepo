# Forex Analysis Telegram Bot

A multi-language Telegram bot for financial market analysis that provides advanced technical indicators and user-friendly trading tools.

## Features

- Multi-language support (Tajik, Russian, Uzbek, Kazakh, English)
- Real-time market analysis with technical indicators:
  - RSI
  - MACD
  - EMA
  - Bollinger Bands
- 30+ currency pairs support
- User authentication system
- Admin panel
- Monitoring system with web interface
- Automatic error recovery
- Detailed market analysis charts

## Quick Deploy

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

## Manual Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/forex-analysis-bot.git
cd forex-analysis-bot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create `.env` file:
```bash
cp .env.example .env
# Edit with your values
```

Required environment variables:
- `BOT_TOKEN`: Telegram bot token from @BotFather
- `DATABASE_URL`: PostgreSQL database URL

## Deployment

### Render.com (Recommended)

1. Fork this repository
2. Create a new Web Service on Render
3. Connect your GitHub repository
4. Add environment variables:
   - `BOT_TOKEN`
   - `DATABASE_URL`
5. Deploy!

### Manual Server Deployment

1. Install requirements:
```bash
sudo apt update
sudo apt install python3 python3-pip postgresql
```

2. Copy files:
```bash
sudo mkdir -p /root/bot
sudo cp -r * /root/bot/
```

3. Install service:
```bash
sudo cp telegram-bot.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable telegram-bot
sudo systemctl start telegram-bot
```

## Development

1. Install development dependencies:
```bash
pip install -r requirements.txt
```

2. Run bot:
```bash
python attached_assets/bot.py
```

3. Monitor via web interface:
```
http://localhost:8081
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

## Support

For support and questions:
- Telegram: @tradeporu
- Website: [TRADEPO.RU](https://tradepo.ru)

## License

This project is licensed under the MIT License - see the LICENSE file for details.