# -*- coding: utf-8 -*-

from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging, datetime, schedule, time

updater = Updater(token='568352615:AAEGpAfoFY1994WDGQRZm7TcHDNeP0WU8_M')
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def after_dark(bot, update):
    bot.set_chat_title(chat_id=update.message.chat_id, title=u"Tildé After Dark")

def good_morning(bot, update):
    bot.set_chat_title(chat_id=update.message.chat_id, title=u"Tildé")

def hey(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="hey")
    schedule.every().day.at("00:00").do(after_dark(bot, update))
    schedule.every().day.at("07:00").do(good_morning(bot, update))

start_handler = CommandHandler('hey', hey)
dispatcher.add_handler(start_handler)

updater.start_polling()
while True:
    schedule.run_pending()
    time.sleep(60)
