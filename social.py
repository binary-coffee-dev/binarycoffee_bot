import os
import telegram

class Telegram:
    def __init__(self):
        self.token = os.environ['TOKEN']
        self.chat_id = os.environ['CHANNEL']

    def post(self, msg):
        bot = telegram.Bot(token=self.token)
        bot.sendMessage(chat_id=self.chat_id, text=msg)
