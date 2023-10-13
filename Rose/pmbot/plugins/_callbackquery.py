from pyrogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup

from ..pmbot.helper import buttons, captcha_buttons, captcha_text

from pyrogram import Client

from ..modules.vars import *

from ..modules import *

from ..import *



@bot.on_callback_query()

def callback_query(Client, CallbackQuery):

    if CallbackQuery.data == "🧊":

        CallbackQuery.edit_message_text(

            captcha_text.PASS_CAPTCHA,

            reply_markup=ReplyKeyboardMarkup(buttons.REPLY_BUTTONS, one_time_keyboard=False, resize_keyboard=True)

        )

        try:

            text = "Congratulations🎉🎉\nYou proved yourself that you are a human!"

            Client.answer_callback_query(CallbackQuery.id, text=text, show_alert=True)

        except Exception as error_pass:

            Client.answer_callback_query(CallbackQuery.id, text=f"Error occurred!!\n\n{error_pass}", show_alert=True)



    elif CallbackQuery.data == "❌":

        CallbackQuery.edit_message_text(

            captcha_text.MULTY_FAIL,

            reply_markup=InlineKeyboardMarkup(captcha_buttons.RELOAD_CAPTCHA)

        )

    elif CallbackQuery.data == "📩" or "🔥" or "🌭" or "🚑" or "🚡" or "💡" or "🔎" or "📈" or "🎆" or "🎎" or "🍧" or "⛑" or "🪀" or "🧸":

        CallbackQuery.edit_message_text(

            captcha_text.FAIL_CAPTCHA,

            reply_markup=InlineKeyboardMarkup(captcha_buttons.WRONG_CAPTCHA)

        ),



    if CallbackQuery.data == "one_star":

        e = CallbackQuery.edit_message_text(

            f"**Bot - Feedback Bot (Sanila Assistant Bot)**\n\nGiven Stars - ⭐(1 star)\nUser - {CallbackQuery.from_user.first_name} {CallbackQuery.from_user.last_name}\nUsername - @{CallbackQuery.from_user.username}\n\n<i>*Your ratings have been sent to the admin. Thank you!</i>"

        )

        try:

            Client.send_message(Config.FEEDBACK_GROUP, f"**<u>New user has been rated a Client</u>**\n\n{e.text}",

                                protect_content=True)

            text = "Thanks for your collaboration❤\n\nThese ratings help us a lot to make our Clients more efficient. These ratings have been shared with the admin.\n\nFeedback Bot."

            Client.answer_callback_query(CallbackQuery.id, text=text, show_alert=True)

        except Exception as error:

            LOGGER(f"Unable to send ratings to the channel\n\nReason- {error}")



    elif CallbackQuery.data == "two_star":

        d = CallbackQuery.edit_message_text(

            f"**Bot - Feedback Bot (Sanila Assistant Bot)**\n\nGiven Stars - ⭐⭐(2 star)\nUser - {CallbackQuery.from_user.first_name} {CallbackQuery.from_user.last_name}\nUsername - @{CallbackQuery.from_user.username}\n\n<i>*Your ratings have been sent to the admin. Thank you!</i>"

        )

        try:

            Client.send_message(Config.FEEDBACK_GROUP, f"**<u>New user has been rated a Client</u>**\n\n{d.text}",

                                protect_content=True)

            text = "Thanks for your collaboration❤\n\nThese ratings help us a lot to make our Clients more efficient. These ratings have been shared with the admin.\n\nFeedback Bot."

            Client.answer_callback_query(CallbackQuery.id, text=text, show_alert=True)

        except Exception as error:

            LOGGER(f"Unable to send ratings to the channel\n\nReason- {error}")



    if CallbackQuery.data == "three_star":

        c = CallbackQuery.edit_message_text(

            f"**Bot - Feedback Bot (Sanila Assistant Bot)**\n\nGiven Stars - ⭐⭐⭐(3 star)\nUser - {CallbackQuery.from_user.first_name} {CallbackQuery.from_user.last_name}\nUsername - @{CallbackQuery.from_user.username}\n\n<i>*Your ratings have been sent to the admin. Thank you!</i>"

        )

        try:

            Client.send_message(Config.FEEDBACK_GROUP, f"**<u>New user has been rated a Client</u>**\n\n{c.text}",

                                protect_content=True)

            text = "Thanks for your collaboration❤\n\nThese ratings help us a lot to make our Clients more efficient. These ratings have been shared with the admin.\n\nFeedback Bot."

            Client.answer_callback_query(CallbackQuery.id, text=text, show_alert=True)

        except Exception as error:

            LOGGER(f"Unable to send ratings to the channel\n\nReason- {error}")



    elif CallbackQuery.data == "four_star":

        b = CallbackQuery.edit_message_text(

            f"**Bot - Feedback Bot (Sanila Assistant Bot)**\n\nGiven Stars - ⭐⭐⭐⭐(4 star)\nUser - {CallbackQuery.from_user.first_name} {CallbackQuery.from_user.last_name}\nUsername - @{CallbackQuery.from_user.username}\n\n<i>*Your ratings have been sent to the admin. Thank you!</i>"

        )

        try:

            Client.send_message(Config.FEEDBACK_GROUP, f"**<u>New user has been rated a Client</u>**\n\n{b.text}",

                                protect_content=True)

            text = "Thanks for your collaboration❤\n\nThese ratings help us a lot to make our Clients more efficient. These ratings have been shared with the admin.\n\nFeedback Bot."

            Client.answer_callback_query(CallbackQuery.id, text=text, show_alert=True)

        except Exception as error:

            LOGGER(f"Unable to send ratings to the channel\n\nReason- {error}")



    if CallbackQuery.data == "five_star":

        a = CallbackQuery.edit_message_text(

            f"**Bot - Feedback Bot (Sanila Assistant Bot)**\n\nGiven Stars - ⭐⭐⭐⭐⭐(5 star)\nUser - {CallbackQuery.from_user.first_name} {CallbackQuery.from_user.last_name}\nUsername - @{CallbackQuery.from_user.username}\n\n<i>*Your ratings have been sent to the admin. Thank you!</i>"

        )

        try:

            Client.send_message(Config.FEEDBACK_GROUP, f"**<u>New user has been rated a Client</u>**\n\n{a.text}",

                                protect_content=True)

            text = "Thanks for your collaboration❤\n\nThese ratings help us a lot to make our Clients more efficient. These ratings have been shared with the admin.\n\nFeedback Bot."

            Client.answer_callback_query(CallbackQuery.id, text=text, show_alert=True)

        except Exception as error:

            LOGGER(f"Unable to send ratings to the channel\n\nReason- {error}")



    ## Telegraph Bot Ratings-------------------------------------------------------------------------------------------------------------

    elif CallbackQuery.data == "one_star_telegraph":

        f = CallbackQuery.edit_message_text(

            f"**Bot - Telegraph Uploader**\n\nGiven Stars - ⭐(1 star)\nUser - {CallbackQuery.from_user.first_name} {CallbackQuery.from_user.last_name}\nUsername - @{CallbackQuery.from_user.username}\n\n<i>*Your ratings have been sent to the admin. Thank you!</i>"

        )

        try:

            Client.send_message(Config.FEEDBACK_GROUP, f"**<u>New user has been rated a Client</u>**\n\n{f.text}",

                                protect_content=True)



            text = "Thanks for your collaboration❤\n\nThese ratings help us a lot to make our Clients more efficient. These ratings have been shared with the admin.\n\nFeedback Bot."

            Client.answer_callback_query(CallbackQuery.id, text=text, show_alert=True)

        except Exception as error:

            LOGGER(f"Unable to send ratings to the channel\n\nReason- {error}")



    elif CallbackQuery.data == "two_star_telegraph":

        f = CallbackQuery.edit_message_text(

            f"**Bot - Telegraph Uploader**\n\nGiven Stars - ⭐⭐(2 star)\nUser - {CallbackQuery.from_user.first_name} {CallbackQuery.from_user.last_name}\nUsername - @{CallbackQuery.from_user.username}\n\n<i>*Your ratings have been sent to the admin. Thank you!</i>"

        )

        try:

            Client.send_message(Config.FEEDBACK_GROUP, f"**<u>New user has been rated a Client</u>**\n\n{f.text}",

                                protect_content=True)

            text = "Thanks for your collaboration❤\n\nThese ratings help us a lot to make our Clients more efficient. These ratings have been shared with the admin.\n\nFeedback Bot."

            Client.answer_callback_query(CallbackQuery.id, text=text, show_alert=True)

        except Exception as error:

            LOGGER(f"Unable to send ratings to the channel\n\nReason- {error}")



    elif CallbackQuery.data == "three_star_telegraph":

        f = CallbackQuery.edit_message_text(

            f"**Bot - Telegraph Uploader**\n\nGiven Stars - ⭐⭐⭐(3 star)\nUser - {CallbackQuery.from_user.first_name} {CallbackQuery.from_user.last_name}\nUsername - @{CallbackQuery.from_user.username}\n\n<i>*Your ratings have been sent to the admin. Thank you!</i>"

        )

        try:

            Client.send_message(Config.FEEDBACK_GROUP, f"**<u>New user has been rated a Client</u>**\n\n{f.text}",

                                protect_content=True)

            text = "Thanks for your collaboration❤\n\nThese ratings help us a lot to make our Clients more efficient. These ratings have been shared with the admin.\n\nFeedback Bot."

            Client.answer_callback_query(CallbackQuery.id, text=text, show_alert=True)

        except Exception as error:

            LOGGER(f"Unable to send ratings to the channel\n\nReason- {error}")



    elif CallbackQuery.data == "four_star_telegraph":

        f = CallbackQuery.edit_message_text(

            f"**Bot - Telegraph Uploader**\n\nGiven Stars - ⭐⭐⭐⭐(4 star)\nUser - {CallbackQuery.from_user.first_name} {CallbackQuery.from_user.last_name}\nUsername - @{CallbackQuery.from_user.username}\n\n<i>*Your ratings have been sent to the admin.  Thank you!</i>"

        )

        try:

            Client.send_message(Config.FEEDBACK_GROUP, f"**<u>New user has been rated a Client</u>**\n\n{f.text}",

                                protect_content=True)

            text = "Thanks for your collaboration❤\n\nThese ratings help us a lot to make our Clients more efficient. These ratings have been shared with the admin.\n\nFeedback Bot."

            Client.answer_callback_query(CallbackQuery.id, text=text, show_alert=True)

        except Exception as error:

            LOGGER(f"Unable to send ratings to the channel\n\nReason- {error}")



    elif CallbackQuery.data == "five_star_telegraph":

        f = CallbackQuery.edit_message_text(

            f"**Bot - Telegraph Uploader**\n\nGiven Stars - ⭐⭐⭐⭐⭐(5 star)\nUser - {CallbackQuery.from_user.first_name} {CallbackQuery.from_user.last_name}\nUsername - @{CallbackQuery.from_user.username}\n\n<i>*Your ratings have been sent to the admin. Thank you!</i>"

        )

        try:

            Client.send_message(Config.FEEDBACK_GROUP, f"**<u>New user has been rated a Client</u>**\n\n{f.text}",

                                protect_content=True)

            text = "Thanks for your collaboration❤\n\nThese ratings help us a lot to make our Clients more efficient. These ratings have been shared with the admin.\n\nFeedback Bot."

            Client.answer_callback_query(CallbackQuery.id, text=text, show_alert=True)

        except Exception as error:

            LOGGER(f"Unable to send ratings to the channel\n\nReason- {error}")



    ## Song Downloader Ratings-------------------------------------------------------------------------------------------

    elif CallbackQuery.data == "one_star_song":

        f = CallbackQuery.edit_message_text(

            f"**Bot - Song Downloader**\n\nGiven Stars - ⭐(1 star)\nUser - {CallbackQuery.from_user.first_name} {CallbackQuery.from_user.last_name}\nUsername - @{CallbackQuery.from_user.username}\n\n<i>*Your ratings have been sent to the admin. Thank you!</i>"

        )

        try:

            Client.send_message(Config.FEEDBACK_GROUP, f"**<u>New user has been rated a Client</u>**\n\n{f.text}",

                                protect_content=True)



            text = "Thanks for your collaboration❤\n\nThese ratings help us a lot to make our Clients more efficient. These ratings have been shared with the admin.\n\nFeedback Bot."

            Client.answer_callback_query(CallbackQuery.id, text=text, show_alert=True)

        except Exception as error:

            LOGGER(f"Unable to send ratings to the channel\n\nReason- {error}")



    elif CallbackQuery.data == "two_star_song":

        f = CallbackQuery.edit_message_text(

            f"**Bot - Song Downloader**\n\nGiven Stars - ⭐⭐(2 star)\nUser - {CallbackQuery.from_user.first_name} {CallbackQuery.from_user.last_name}\nUsername - @{CallbackQuery.from_user.username}\n\n<i>*Your ratings have been sent to the admin. Thank you!</i>"

        )

        try:

            Client.send_message(Config.FEEDBACK_GROUP, f"**<u>New user has been rated a Client</u>**\n\n{f.text}",

                                protect_content=True)



            text = "Thanks for your collaboration❤\n\nThese ratings help us a lot to make our Clients more efficient. These ratings have been shared with the admin.\n\nFeedback Bot."

            Client.answer_callback_query(CallbackQuery.id, text=text, show_alert=True)

        except Exception as error:

            LOGGER(f"Unable to send ratings to the channel\n\nReason- {error}")



    elif CallbackQuery.data == "three_star_song":

        f = CallbackQuery.edit_message_text(

            f"**Bot - Song Downloader**\n\nGiven Stars - ⭐⭐⭐(3 star)\nUser - {CallbackQuery.from_user.first_name} {CallbackQuery.from_user.last_name}\nUsername - @{CallbackQuery.from_user.username}\n\n<i>*Your ratings have been sent to the admin. Thank you!</i>"

        )

        try:

            Client.send_message(Config.FEEDBACK_GROUP, f"**<u>New user has been rated a Client</u>**\n\n{f.text}",

                                protect_content=True)



            text = "Thanks for your collaboration❤\n\nThese ratings help us a lot to make our Clients more efficient. These ratings have been shared with the admin.\n\nFeedback Bot."

            Client.answer_callback_query(CallbackQuery.id, text=text, show_alert=True)

        except Exception as error:

            LOGGER(f"Unable to send ratings to the channel\n\nReason- {error}")



    elif CallbackQuery.data == "four_star_song":

        f = CallbackQuery.edit_message_text(

            f"**Bot - Song Downloader**\n\nGiven Stars - ⭐⭐⭐⭐(4 star)\nUser - {CallbackQuery.from_user.first_name} {CallbackQuery.from_user.last_name}\nUsername - @{CallbackQuery.from_user.username}\n\n<i>*Your ratings have been sent to the admin. Thank you!</i>"

        )

        try:

            Client.send_message(Config.FEEDBACK_GROUP, f"**<u>New user has been rated a Client</u>**\n\n{f.text}",

                                protect_content=True)



            text = "Thanks for your collaboration❤\n\nThese ratings help us a lot to make our Clients more efficient. These ratings have been shared with the admin.\n\nFeedback Bot."

            Client.answer_callback_query(CallbackQuery.id, text=text, show_alert=True)

        except Exception as error:

            LOGGER(f"Unable to send ratings to the channel\n\nReason- {error}")



    elif CallbackQuery.data == "five_star_song":

        f = CallbackQuery.edit_message_text(

            f"**Bot - Song Downloader**\n\nGiven Stars - ⭐⭐⭐⭐⭐(5 star)\nUser - {CallbackQuery.from_user.first_name} {CallbackQuery.from_user.last_name}\nUsername - @{CallbackQuery.from_user.username}\n\n<i>*Your ratings have been sent to the admin. Thank you!</i>"

        )

        try:

            Client.send_message(Config.FEEDBACK_GROUP, f"**<u>New user has been rated a Client</u>**\n\n{f.text}",

                                protect_content=True)



            text = "Thanks for your collaboration❤\n\nThese ratings help us a lot to make our Clients more efficient. These ratings have been shared with the admin.\n\nFeedback Bot."

            Client.answer_callback_query(CallbackQuery.id, text=text, show_alert=True)

        except Exception as error:

            LOGGER(f"Unable to send ratings to the channel\n\nReason- {error}")



    ## Torrent Downloader Ratings------------------------------------------------------------------------------------------

    elif CallbackQuery.data == "one_star_torrent":

        f = CallbackQuery.edit_message_text(

            f"**Bot - Torrent Uploader**\n\nGiven Stars - ⭐(1 star)\nUser - {CallbackQuery.from_user.first_name} {CallbackQuery.from_user.last_name}\nUsername - @{CallbackQuery.from_user.username}\n\n<i>*Your ratings have been sent to the admin. Thank you!</i>"

        )

        try:

            Client.send_message(Config.FEEDBACK_GROUP, f"**<u>New user has been rated a Client</u>**\n\n{f.text}",

                                protect_content=True)



            text = "Thanks for your collaboration❤\n\nThese ratings help us a lot to make our Clients more efficient. These ratings have been shared with the admin.\n\nFeedback Bot."

            Client.answer_callback_query(CallbackQuery.id, text=text, show_alert=True)

        except Exception as error:

            LOGGER(f"Unable to send ratings to the channel!!! {error}")



    elif CallbackQuery.data == "two_star_torrent":

        f = CallbackQuery.edit_message_text(

            f"**Bot - Torrent Uploader**\n\nGiven Stars - ⭐⭐(2 star)\nUser - {CallbackQuery.from_user.first_name} {CallbackQuery.from_user.last_name}\nUsername - @{CallbackQuery.from_user.username}\n\n<i>*Your ratings have been sent to the admin. Thank you!</i>"

        )

        try:

            Client.send_message(Config.FEEDBACK_GROUP, f"**<u>New user has been rated a Client</u>**\n\n{f.text}",

                                protect_content=True)



            text = "Thanks for your collaboration❤\n\nThese ratings help us a lot to make our Clients more efficient. These ratings have been shared with the admin.\n\nFeedback Bot."

            Client.answer_callback_query(CallbackQuery.id, text=text, show_alert=True)

        except Exception as error:

            LOGGER(f"Unable to send ratings to the channel\n\nReason- {error}")



    elif CallbackQuery.data == "three_star_torrent":

        f = CallbackQuery.edit_message_text(

            f"**Bot - Torrent Uploader**\n\nGiven Stars - ⭐⭐⭐(3 star)\nUser - {CallbackQuery.from_user.first_name} {CallbackQuery.from_user.last_name}\nUsername - @{CallbackQuery.from_user.username}\n\n<i>*Your ratings have been sent to the admin. Thank you!</i>"

        )

        try:

            Client.send_message(Config.FEEDBACK_GROUP, f"**<u>New user has been rated a Client</u>**\n\n{f.text}",

                                protect_content=True)



            text = "Thanks for your collaboration❤\n\nThese ratings help us a lot to make our Clients more efficient. These ratings have been shared with the admin.\n\nFeedback Bot."

            Client.answer_callback_query(CallbackQuery.id, text=text, show_alert=True)

        except Exception as error:

            print(f"Unable to send ratings to the channel\n\nReason- {error}")



    elif CallbackQuery.data == "four_star_torrent":

        f = CallbackQuery.edit_message_text(

            f"**Bot - Torrent Uploader**\n\nGiven Stars - ⭐⭐⭐⭐(4 star)\nUser - {CallbackQuery.from_user.first_name} {CallbackQuery.from_user.last_name}\nUsername - @{CallbackQuery.from_user.username}\n\n<i>*Your ratings have been sent to the admin. Thank you!</i>"

        )

        try:

            Client.send_message(Config.FEEDBACK_GROUP, f"**<u>New user has been rated a Client</u>**\n\n{f.text}",

                                protect_content=True)



            text = "Thanks for your collaboration❤\n\nThese ratings help us a lot to make our Clients more efficient. These ratings have been shared with the admin.\n\nFeedback Bot."

            Client.answer_callback_query(CallbackQuery.id, text=text, show_alert=True)

        except Exception as error:

            LOGGER(f"Unable to send ratings to the channel\n\nReason- {error}")



    elif CallbackQuery.data == "five_star_torrent":

        f = CallbackQuery.edit_message_text(

            f"**Bot - Torrent Uploader**\n\nGiven Stars - ⭐⭐⭐⭐⭐(5 star)\nUser - {CallbackQuery.from_user.first_name} {CallbackQuery.from_user.last_name}\nUsername - @{CallbackQuery.from_user.username}\n\n<i>*Your ratings have been sent to the admin. Thank you!</i>"

        )

        try:

            Client.send_message(Config.FEEDBACK_GROUP, f"**<u>New user has been rated a Client</u>**\n\n{f.text}",

                                protect_content=True)



            text = "Thanks for your collaboration❤\n\nThese ratings help us a lot to make our Clients more efficient. These ratings have been shared with the admin.\n\nFeedback Bot."

            Client.answer_callback_query(CallbackQuery.id, text=text, show_alert=True)

        except Exception as error:

            LOGGER(f"Unable to send ratings to the channel\n\nReason- {error}")
