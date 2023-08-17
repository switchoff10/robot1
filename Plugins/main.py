import os
from pyrogram import Client

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6679522961:AAEwskarbPC0TfsbUlU__cHyq32yZ7f9VOc")
APP_ID = int(os.environ.get("APP_ID", "27735785"))
API_HASH = os.environ.get("API_HASH", "4c96eea778ecf7c3ac25e3e8682259ae")
plugins = dict(root="Plugins")
app = Client(api_id=APP_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             plugins="Plugins"
             )
app.run()