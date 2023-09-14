from pyrogram import Client, idle, filters
from pyrogram.types import Message
from tech import *


@Client.on_message(filters.private & filters.command("start"))
async def start_bot(_, msg: Message):
    form = await _.send_message(msg.chat.id, f"hello")
    
@Client.on_message(filters.private & filters.command("form"))
async def form_bot(_, msg: Message):
    try:
        cek = await _.ask(msg.chat.id, "kirim string")
        await _.send_message(msg.chat.id, f"string kamu\n{cek}")
    except Exception as ex:
        print('Mistakes for connection')
        print(ex)
