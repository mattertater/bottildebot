# -*- coding: utf-8 -*-

from telegram.ext import Updater
from telegram.ext import CommandHandler
import telegram, logging, datetime, schedule, time

bot = telegram.bot(token='token')
updater = Updater(token='token')
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def after_dark():
    bot.set_chat_title(chat_id='-228400508', title=u"Tildé After Dark")

def good_morning():
    bot.set_chat_title(chat_id='-228400508', title=u"Tildé")

def hey(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="hey")

schedule.every().day.at("00:00").do(after_dark(), "midnight name change")
schedule.every().day.at("07:00").do(good_morning(), "morning name change")

start_handler = CommandHandler('hey', hey)
dispatcher.add_handler(start_handler)

updater.start_polling()
while True:
    schedule.run_pending()
    time.sleep(60)
