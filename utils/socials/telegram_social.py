import os

import telebot
from telebot.types import (Message, Chat)

from utils.socials.base_social import SocialAdapter

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
TELEGRAM_CHANNEL = os.environ.get('TELEGRAM_CHANNEL')


class TelegramAdapter(SocialAdapter):

    def __init__(self):
        self.bot = telebot.TeleBot(TELEGRAM_TOKEN)

    def post(self, msg):
        try:
            self.bot.send_message(chat_id=TELEGRAM_CHANNEL, text=msg)
        except:
            pass
