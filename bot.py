from telegram.ext import Updater, CommandHandler
import logging

logger = logging.getLogger('Calendar_Bot')


class CalendarBot:
    def __init__(self, token):
        self.updater = Updater(token=token)
        self.add_bot_handlers()
        self.updater.start_polling(poll_interval=2, timeout=30, read_latency=5)
        self.updater.idle()

    def add_bot_handlers(self):
        dp = self.updater.dispatcher
        dp.add_handler(CommandHandler('start', self.start))
        dp.add_error_handler(self.error)

    def start(self, bot, update):
        bot.send_message(chat_id=update.message.chat_id, text=str(update.message.chat_id))

    @staticmethod
    def error(bot, update, err):
        logger.warning('Update "%s" caused error "%s"' % (update, err))


token = '404672999:AAF2nOfQWL0YL8sbTwuyDsio8B9TEFuV8ZU'
bot = CalendarBot(token)