import asyncio
from pyrogram import Client
from Abg import patch
from tech import config

manage = Client(
  name=":memory:",
  api_id=config.API_ID,
  api_hash=config.API_HASH,
  bot_token=config.BOT_TOKEN,
  plugins={"root": "tech.Manager"},
)
