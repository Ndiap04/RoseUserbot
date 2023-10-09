import asyncio
from pyrogram import Client
from pyrogram.errors import YouBlockedUser
from pyrogram.types import Message
from ..modules.tools import extract_user
from ..modules import *
from ..import *

@app.on_message(commandx(["sg"]) & SUDOERS)
async def sg(client: Client, message: Message):
    args = await extract_user(message)
    lol = await message.edit_text("`Processing...`")
    if args:
        try:
            user = await client.get_users(args)
        except Exception:
            return await lol.edit(f"`Please specify a valid user!`")
    bot = "SangMata_beta_bot"
    try:
        await client.send_message(bot, f"{user.id}")
    except YouBlockedUser:
        await client.unblock_user(bot)
        await client.send_message(bot, f"{user.id}")
    await asyncio.sleep(1)

    async for stalk in client.search_messages(bot, query="Name", limit=1):
        if not stalk:
            await message.edit_text("**Orang Ini Belum Pernah Mengganti Namanya**")
            return
        elif stalk:
            await message.edit(stalk.text)
            await stalk.delete()

    async for stalk in client.search_messages(bot, query="Username", limit=1):
        if not stalk:
            return
        elif stalk:
            await message.reply(stalk.text)
            await stalk.delete()



__NAME__ = "sangmata"
__MENU__ = f"""
**🥀 Sangmata Command:"*

`.sg` [reply user id / username] 
**Mengambil nama history pengguna.**
        
© Rose Userbot
"""
