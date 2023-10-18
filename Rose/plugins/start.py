import html
from ..modules import *
from ..modules.vars import *
from .. import *
from pyrogram.enums import ParseMode
from pyrogram import Client, filters, idle, enums
from pyrogram.types import Message, User
from ..modules.humanbytes import humanbytes
from ..modules.database import Database

log_grub = var.LOG_GROUP_ID
MONGO_DATABASE = var.MONGO_DATABASE
MONGO_NAME = var.MONGO_NAME

db = Database(MONGO_DATABASE, MONGO_NAME) 

IF_TEXT = "<b>📨MEMBER MENGIRIM PESAN</b>\n<b>• From:</b> {}\n<b>• Name:</b> {}\n\n{}\n\n• @CuhatBarengBottyBot"
IF_CONTENT = "<b>Message from:</b> {} \n<b>Name:</b> {}"
LOG_TEXT = "ID: <code>{}</code>\nFirst Name: <a href='tg://user?id={}'>{}{}</a>\nDC ID: <code>{}</code>"

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
      
    # 
    ban_status = await db.get_ban_status(chat_id)
    is_banned = ban_status['is_banned']
    ban_duration = ban_status['ban_duration']
    ban_reason = ban_status['ban_reason']
    if is_banned is True:
        await message.reply_text(f"You are Banned 🚫 to use this bot for **{ban_duration}** day(s) for the reason __{ban_reason}__ \n\n**Message from the admin 🤠**")
        return
      
    await bot.send_message(
        chat_id=log_grub,
        text=LOG_TEXT.format(message.chat.id,message.chat.id,message.chat.first_name,message.chat.last_name,message.chat.dc_id),
        parse_mode=ParseMode.HTML,
    )
    await message.reply_text(
        text="**Hi {}!**\n".format(message.chat.first_name)+START,
        reply_markup=InlineKeyboardMarkup([
            [ InlineKeyboardButton(text="🛠SUPPORT🛠", url=f"{C.SUPPORT_GROUP}"), InlineKeyboardButton(text="📮UPDATES📮", url=f"{C.UPDATE_CHANNEL}")]
        ])
    )
        
@bot.on_message(filters.private & filters.text)
async def pm_text(bot, message):
    if message.from_user.id == log_grub:
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
       
