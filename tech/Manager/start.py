from pyrogram import *
from pyrogram.types import *
from tech import manage

@manage.on_message(filters.private & filters.command("start"))
async def start_bot(zen: manage, message: Message):
    await zen.send_message(message.from_user.id, f"👋🏻 Hallo")
