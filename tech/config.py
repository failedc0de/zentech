from os import getenv

from dotenv import load_dotenv

load_dotenv("config.env")

API_ID = int(getenv("API_ID", "3563677"))
API_HASH = getenv("API_HASH", "483c51115c56b7d44111bd0fe31cc9cf")
BOT_TOKEN = getenv("BOT_TOKEN", "6166148172:AAF2yABKyEF3nOLroJIuzO7zSAKEvuaAJxg")
#BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
#MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://knsgnwn:knsgnwn@cluster0.jsdln69.mongodb.net/?retryWrites=true&w=majority")
