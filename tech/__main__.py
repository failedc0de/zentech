import asyncio

from pyrogram import Client, idle
from pyromod import listen 
from tech import manage


async def start():
    await manage.start()
    await idle()
    
manage.run(start())
