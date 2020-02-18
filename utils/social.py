import telegram


class Telegram:
    def __init__(self, token, channel_id):
        self.token = token
        self.chat_id = channel_id

    def post(self, msg):
        bot = telegram.Bot(token=self.token)
        bot.sendMessage(chat_id=self.chat_id, text=msg)
