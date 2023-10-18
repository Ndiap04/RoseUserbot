import html
from ..modules import *
from ..modules.vars import *
from .. import *
from pyrogram.enums import ParseMode
from pyrogram import Client, filters, idle, enums
from pyrogram.types import Message, User
from ..modules.humanbytes import humanbytes

IF_TEXT = "<b>💬 MEMBER MENGIRIM PESAN</b>\n<b>Message from:</b> {}\n<b>Name:</b> {}\n\n{}\n\nBot @CuhatBarengBottyBot"
IF_CONTENT = "<b>Message from:</b> {} \n<b>Name:</b> {}"

log_grub = var.LOG_GROUP_ID

@bot.on_message(filters.command('start') & (filters.private | filters.group))
async def start(bot, message):
    chat_id = message.from_user.id
    # Adding to DB
    if not await db.is_user_exist(chat_id):
        data = await bot.get_me()
        BOT_USERNAME = data.username
        await db.add_user(chat_id)
        await bot.send_message(
            LOG_GROUP_ID,
            f"#NEWUSER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) started @{BOT_USERNAME} !!",
        )
        return
        
@bot.on_message(filters.private & filters.text)
async def pm_text(bot, message):
    if message.from_user.id == owner_id:
        await reply_text(bot, message)
        return
    info = await bot.get_users(user_ids=message.from_user.id)
    reference_id = int(message.chat.id)
    await bot.send_message(
        chat_id=log_grub,
        text=IF_TEXT.format(reference_id, info.first_name, message.text),
        parse_mode=ParseMode.HTML,
    )

@bot.on_message(filters.user(log_grub) & filters.text & filters.private)
async def reply_text(bot, message):
    reference_id = True
    if message.reply_to_message is not None:
        file = message.reply_to_message
        try:
            reference_id = file.text.split()[2]
        except Exception:
            pass
        try:
            reference_id = file.caption.split()[2]
        except Exception:
            pass
        await bot.send_message(
            text=message.text,
            chat_id=int(reference_id)
        )  
       
