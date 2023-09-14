import pymysql
from pyrogram import Client, idle, filters
from pyrogram.types import Message
from tech import *


@manage.on_message(filters.private & filters.command("start"))
async def start_bot(_, msg: Message):
    form = await _.send_message(msg.chat.id, f"hello")
    
@manage.on_message(filters.private & filters.command("form"))
async def form_bot(_, msg: Message):
    form = await _.send_message(msg.chat.id, f"tunggu sebentar")
    try:
        a = msg.chat.id
        b = await _.ask(msg.chat.id, "kirim string session kamu")
        await _.send_message(msg.chat.id, f"{b}")
    except Exception as ex:
        print('Mistakes for connection')
        print(ex)
