
from pyrogram import enums

from pyrogram.types import ReplyKeyboardMarkup

from ..pmbot.helper import ratings

from pyrogram import Client, filters

from ..import *

from ..modules import *

# Rating bots



@bot.on_message(filters.regex(pattern="Rate Bot"))

def reply_to_rate_bots(bot, message):

    bot.send_chat_action(message.chat.id, enums.ChatAction.SPEAKING)

    text = ratings.RATINGS_TEXT

    reply_markup = ReplyKeyboardMarkup(ratings.RATINGS_BUTTONS, resize_keyboard=True, one_time_keyboard=False)

    message.reply(

        text=text,

        reply_markup=reply_markup,

        disable_web_page_preview=True

    )





# Rating bots



@bot.on_message(filters.regex(pattern="Assistant Bot"))

def reply_to_rating_assistant(bot, message):

    reply_markup = ratings.RATING_BOT_FEEDBACK_BOT

    bot.send_message(message.chat.id,

                     f"How many stars would you like to give to **{message.text}**??\n\n<i>*Note - These ratings will be reset after you rate but these ratings will share with the admin(developer)</i>",

                     reply_markup=reply_markup)





@bot.on_message(filters.regex(pattern="Torrent Bot"))

def reply_to_rating_torrent(bot, message):

    reply_markup = ratings.RATING_BOT_TORRENT

    bot.send_message(message.chat.id,

                     f"How many stars would you like to give to **{message.text}**??\n\n<i>*Note - These ratings will be reset after you rate but these ratings will share with the admin(developer)</i>",

                     reply_markup=reply_markup)





@bot.on_message(filters.regex(pattern="Telegraph Bot"))

def reply_to_rating_telegraph(bot, message):

    reply_markup = ratings.RATING_BOT_TELEGRAPH

    bot.send_message(message.chat.id,

                     f"How many stars would you like to give to **{message.text}**??\n\n<i>*Note - These ratings will be reset after you rate but these ratings will share with the admin(developer)</i>",

                     reply_markup=reply_markup)





@bot.on_message(filters.regex(pattern="Song Bot"))

async def reply_to_rating_song(bot, message):

    reply_markup = ratings.RATING_BOT_SONG

    await bot.send_message(message.chat.id,

                           f"How many stars would you like to give to **{message.text}**??\n\n<i>*Note - These ratings will be reset after you rate but these ratings will share with the admin(developer)</i>",

                           reply_markup=reply_markup)
