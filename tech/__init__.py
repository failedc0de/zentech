import asyncio
from pyrogram import Client
from motor.motor_asyncio import AsyncIOMotorClient as pantek
from Abg import patch
from tech import config

MONGODB_CLI = pantek("mongodb+srv://khansagunawan157:UDg0BmbVKhHlOpGv@cluster0.zyfsas1.mongodb.net/?retryWrites=true&w=majority")
db = MONGODB_CLI.tech

manage = Client(
  name=":memory:",
  api_id=config.API_ID,
  api_hash=config.API_HASH,
  bot_token=config.BOT_TOKEN,
  plugins={"root": "tech.Manager"},
)
