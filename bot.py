import os
import time
import requests
import json

from utils.social import Telegram
from utils.data import get_data_adapter

# ENVIRONMENT VARIABLES
REFRESH_TIME = int(os.environ.get('REFRESH_TIME')) if os.environ.get('REFRESH_TIME') else 60
RSS_FEED = os.environ.get('RSS_FEED')
TOKEN = os.environ.get('TOKEN')
CHANNEL = os.environ.get('CHANNEL')
DATA_ADAPTER = os.environ.get('DATA_ADAPTER') if os.environ.get('DATA_ADAPTER') else 'JsonAdapter'
DATA_PATH = os.environ.get('DATA_PATH') if\
    os.environ.get('DATA_PATH') else\
    os.path.join(os.path.dirname(__file__), 'data')


# INITIALIZING COMPONENTS
data_adapter = get_data_adapter(data_path=DATA_PATH, strategy=DATA_ADAPTER)
telegram_channel = Telegram(token=TOKEN, channel_id=CHANNEL)


while True:
    data = requests.get(RSS_FEED)
    content = json.loads(data.content)

    new_posts = data_adapter.add_and_get_new_items(items=content['items'])
    if len(new_posts) > 0:
        for i in new_posts:
            url = i.get('url') if i.get('url') is not None else ''
            summary = i.get('summary') if i.get('summary') is not None else\
                i.get('title') if i.get('title') is not None else ''
            telegram_channel.post('{}\n{}'.format(summary, url))

    time.sleep(REFRESH_TIME)
