import asyncio

from pyrogram import Client, idle
from Abg import patch
from tech import config
from tech import manage

manage = Client(
  name=":memory:",
  api_id=config.API_ID,
  api_hash=config.API_HASH,
  bot_token=config.BOT_TOKEN,
  plugins={"root": "tech.Manager"},
)

async def start():
    await manage.start()
    await idle()
    
manage.run(start())
