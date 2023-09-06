from pyrogram import Client, idle, filters
from pyrogram.types import Message
from tech import manage

@manage.on_message(filters.private & filters.command("start"))
async def start_bot(zen: manage, msg: Message):
    await zen.send_message(msg.chat.id, f"👋🏻 Hallo")
