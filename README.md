# Instagram Bot

A simple Instagram bot that logs in, stays online, follows a user, and sends them a direct message.

## Features

- ✓ Login to Instagram
- ✓ Stay online (keep-alive mechanism)
- ✓ Follow users
- ✓ Send direct messages

## Installation

1. Clone the repository:
```bash
git clone https://github.com/blxssedsoul11-afk/instagram-bot.git
cd instagram-bot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your Instagram credentials:
```bash
cp .env.example .env
```

4. Edit `.env` and add your Instagram username and password:
```
INSTAGRAM_USERNAME=your_username
INSTAGRAM_PASSWORD=your_password
```

## Usage

Run the bot:
```bash
python bot.py
```

The bot will:
1. Login to Instagram
2. Follow @xristovv_official77
3. Send the message "Здр брат"
4. Stay online by sending periodic requests every 30 seconds

## Current Configuration

- **Target User**: @xristovv_official77
- **Message**: Здр брат
- **Keep-alive Interval**: 30 seconds

## Customization

To modify the target user or message, edit the following in `bot.py`:
```python
TARGET_USERNAME = '@xristovv_official77'
TARGET_MESSAGE = 'Здр брат'
```

To change the keep-alive interval, modify:
```python
stay_online(client, interval=30)  # Change 30 to desired seconds
```

## Notes

- Keep your `.env` file private and never commit it to git
- Instagram may rate-limit or flag accounts for bot activity
- Use responsibly and in accordance with Instagram's Terms of Service
- The bot uses `instagrapi` which is an unofficial Instagram API library

## License

MIT
