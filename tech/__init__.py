import asyncio
from pyrogram import Client
from pyromod import listen 
from tech import config

import pymysql
 
 
# establish connection to MySQL
connection = pymysql.connect(
    host="localhost",
    user="id21233481_khansa",
    password="Knsgnwn#1",
    port=3306,
    db="id21233481_zenblogger"
)
 
# make cursor for establish connection
mycursor = connection.cursor()
manage = Client(
  name=":memory:",
  api_id=config.API_ID,
  api_hash=config.API_HASH,
  bot_token=config.BOT_TOKEN,
  plugins={"root": "tech.Manager"},
)
