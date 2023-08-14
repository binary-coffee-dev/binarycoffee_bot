from utils.socials.telegram_social import TelegramAdapter
from utils.socials.twitter_social import TwitterAdapter


class Socials:
    def __init__(self):
        self.socials = [TelegramAdapter(), TwitterAdapter()]

    def post(self, msg):
        for social in self.socials:
            social.post(msg)
