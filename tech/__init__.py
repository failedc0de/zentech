import asyncio
from pyrogram import Client
from pyromod import listen 
from tech import config
# from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

# MONGODB_CLI = MongoClient(" MongoDB ")
# db = MONGODB_CLI.userbot

manage = Client(
  ":memory:",
  api_id=config.API_ID,
  api_hash=config.API_HASH,
  bot_token=config.BOT_TOKEN,
  plugins={"root": "tech.Manager"},
)
