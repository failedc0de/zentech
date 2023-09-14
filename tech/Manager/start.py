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
    a = msg.chat.id
    try:
        connection = pymysql.connect(host='localhost', user='id21233481_khansa', database='id21233481_zenblogger', password='Knsgnwn#1')
        print('success')
        cursor = connection.cursor()
        anj = f"INSERT INTO `dashboard_user` (chat_id) VALUES (a)"
        cursor.execute(anj)
        connection.commit()
        connection.close() 
        await form.edit("berhasil")
    except Exception as ex:
        print('Mistakes for connection')
        print(ex)
