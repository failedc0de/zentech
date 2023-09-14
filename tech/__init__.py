import asyncio
from pyrogram import Client
from pyromod import listen 
from tech import config

import pymysql
con = pymysql.connect('localhost', 'id21233481_khansa', 
    'Knsgnwn#1', 'id21233481_zenblogger')

manage = Client(
  name=":memory:",
  api_id=config.API_ID,
  api_hash=config.API_HASH,
  bot_token=config.BOT_TOKEN,
  plugins={"root": "tech.Manager"},
)
