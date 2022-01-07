import os
from pyrogram import Client

bot_token = "5067445854:AAFe_Em5hNWTQbaDq5kFfWNsR9JPe5M6RJc"
api_id = 2171111
api_hash = "fd7acd07303760c52dcc0ed8b2f73086"

plugins = dict(
    root="plugins"
)

Bot = Client(
    "class",
    bot_token=bot_token,
    api_id=api_id,
    api_hash=api_hash,
    plugins=plugins
)
print("starting..raaa")
Bot.run()
