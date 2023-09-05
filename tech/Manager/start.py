from pyrogram import *
from pyrogram.types import *
from tech import manage

@manage.on_message(filters.private & filters.command("start"))
async def start_bot(zen: manage, msg: Message):
    user_id = msg.chat.id
    return await zen.send_message(user_id, f"👋🏻 Hallo {msg.from_user.mention}")
