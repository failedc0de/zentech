import os, asyncio
from pyrogram import Client, idle, filters
from pyrogram.types import Message

cmd = "."

@Client.on_message(filters.command(["tech"], cmd) & filters.me)
async def zentectth(client: Client, message: Message):
    await message.edit("I")
    await asyncio.sleep(0.5)
    await message.edit("am")
    await asyncio.sleep(0.5)
    await message.edit("zentech")
    await asyncio.sleep(0.5)
    await message.edit("Userbot")
    await asyncio.sleep(3)
    await message.edit("Zentecth-Ubot\nPOWERED by @phobiakalian")
