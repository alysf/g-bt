from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler


def start(bot, update):
    keyboard = [[InlineKeyboardButton("fffff", callback_data='@liberbot_iraq'),
                InlineKeyboardButton("gggggg", callback_data='@livil')],
                [InlineKeyboardButton("rrrrrr", callback_data='erwerwer')],
                [InlineKeyboardButton("dfgdfgdfg",callback_data ='yertrtertr')]]



    r = InlineKeyboardMarkup(keyboard)
    bot.sendMessage(chat_id=update.message.chat_id, text="tertdgdfgdf", reply_markup=r)


def button(bot, update):
    query = update.callback_query

    bot.editMessageText(text="dfgdfgdfgdfgdf: %s " % query.data,
                        chat_id=query.message.chat_id,
                        message_id=query.message.message_id)
def help(bot,update):
          bot.sendMessage(chat_id=update.message.chat_id,text="gdfgdf dfgdfgdf /start gdfgdfgdfg")


updater = Updater("293882448:AAH8fMtJ6QEA4ZAo4O0Zw62HpnG1sy3_J_A")
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(button))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.start_polling()
