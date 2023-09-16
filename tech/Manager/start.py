from pyrogram import Client, idle, filters
from pyrogram.types import Message
from tech import manage as app
from tech.Database.test import get_authuser_names, save_authuser, delete_authuser, extract_user

@Client.on_message(filters.private & filters.command("start"))
async def start_bot(_, ctx: Message):
    form = await _.send_message(ctx.chat.id, f"hello")
    
@Client.on_message(filters.private & filters.command("form"))
async def form_bot(_, ctx: Message):
    try:
        cek = await ctx.chat.ask("Type your string session")
        await _.send_message(ctx.chat.id, f"string kamu\n{cek.text}")
    except Exception as ex:
        print('Mistakes for connection')
        print(ex)
        
async def int_to_alpha(user_id: int) -> str:
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    text = ""
    user_id = str(user_id)
    for i in user_id:
        text += alphabet[int(i)]
    return text
    
@Client.on_message(filters.command("auth") & filters.group & filters.private)
async def auth(client: Client, message: Message, _):
    chat_id = message.chat.id
    userid = await extract_user(message)
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text("😕 Maaf, **Saya tidak bisa** menemukan pengguna ini!\n\n» coba beri saya id atau username pengguna tersebut")
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        user_id = message.from_user.id
        token = await int_to_alpha(user.id)
        from_user_name = message.from_user.first_name
        from_user_id = message.from_user.id
        _check = await get_authuser_names(message.chat.id)
        count = 0 
        for smex in _check:
            count += 1
        if int(count) == 20:
            return await message.reply_text("😕 Anda hanya dapat memiliki 20 Pengguna dalam daftar pengguna **resmi** grup Anda.")
        if token not in _check:
            assis = {
                "auth_user_id": user.id,
                "auth_name": user.first_name,
                "admin_id": from_user_id,
                "admin_name": from_user_name,
            }
            await save_authuser(message.chat.id, token, assis)
            mention = user.mention
            await message.reply_text(f"🧙 **menambahkan** {mention} ke **daftar pengguna resmi**, mulai sekarang dia bisa **menggunakan** perintah **Admin.**")
            return
        else:
            return await message.reply_text(f"{mention} sudah ada di **daftar pengguna resmi** dan dia dapat menggunakan **perintah admin.**")
    from_user_id = message.from_user.id
    user_id = message.reply_to_message.from_user.id
    user_name = message.reply_to_message.from_user.first_name
    token = await int_to_alpha(user_id)
    from_user_name = message.from_user.first_name
    _check = await get_authuser_names(message.chat.id)
    count = 0
    for smex in _check:
        count += 1
    if int(count) == 20:
        return await message.reply_text("😕 Anda hanya dapat memiliki 20 Pengguna dalam daftar pengguna **resmi** grup Anda.")
    if token not in _check:
        assis = {
            "auth_user_id": user_id,
            "auth_name": user_name,
            "admin_id": from_user_id,
            "admin_name": from_user_name,
        }
        await save_authuser(message.chat.id, token, assis)
        await message.reply_text(f"🧙 **menambahkan** {message.reply_to_message.from_user.mention} ke **daftar pengguna resmi**, mulai sekarang dia bisa **menggunakan** perintah **Admin.**")
        return
    else:
        return await message.reply_text(
            f"{message.reply_to_message.from_user.mention} sudah ada di **daftar pengguna resmi** dan dia dapat menggunakan **perintah admin.**")
