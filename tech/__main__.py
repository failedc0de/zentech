import asyncio

from pyrogram import Client, idle
from pyromod import listen 
from .. import config
# from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

# MONGODB_CLI = MongoClient(" MongoDB ")
# db = MONGODB_CLI.userbot

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
