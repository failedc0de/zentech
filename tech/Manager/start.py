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
        b = await bot.ask(msg.chat.id, "kirim string session kamu")
        c = msg.from_user.username
        d = "member"
        e = await bot.ask(msg.chat.id, "buatlah password")
        f = msg.from_user.first_name
        try:
            connection = pymysql.connect(host='localhost', user='id21233481_khansa', database='id21233481_zenblogger', password='Knsgnwn#1')
            print('success')
            try:
                cursor = connection.cursor()
                anj = f"INSERT INTO `dashboard_user` (chat_id, user_name, user_role, user_password, user_full_name, user_stringsession) VALUES ({a}, {b}, {c}, {d}, {f}, {g})"
                cursor.execute(anj)
                connection.commit()
        finally:
            connection.close() 
            await form.edit("berhasil")
    except Exception as ex:
        print('Mistakes for connection')
        print(ex)
