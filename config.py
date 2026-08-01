import os

# Telegram Bot Token
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# Admin Telegram User ID
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

# Force Join Channels
FORCE_CHANNELS = [
    "@your_channel_1",
    "@your_channel_2",
]
