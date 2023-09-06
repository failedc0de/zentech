from pyrogram import Client, idle, filters
from pyrogram.types import Message
from tech import *

@manage.on_message(filters.private & filters.command("start"))
async def start_bot(_, msg: Message):
    await _.send_message(msg.chat.id, f"👋🏻 Hallo")
