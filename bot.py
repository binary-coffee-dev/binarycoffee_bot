import os
import time
import requests
import json

from utils.social import Socials
from utils.data import get_data_adapter

# ENVIRONMENT VARIABLES BEGIN
REFRESH_TIME = int(os.environ.get('REFRESH_TIME')) if os.environ.get('REFRESH_TIME') else 60
RSS_FEED = os.environ.get('RSS_FEED')

DATA_ADAPTER = os.environ.get('DATA_ADAPTER') if os.environ.get('DATA_ADAPTER') else 'MemoryAdapter'
DATA_PATH = os.environ.get('DATA_PATH') if \
    os.environ.get('DATA_PATH') else \
    os.path.join(os.path.dirname(__file__), 'data')
DATABASE_HOST = os.environ.get('DATABASE_HOST') if os.environ.get('DATABASE_HOST') else None
DATABASE_PORT = int(os.environ.get('DATABASE_PORT')) if os.environ.get('DATABASE_PORT') else None
DATABASE_NAME = os.environ.get('DATABASE_NAME') if os.environ.get('DATABASE_NAME') else None
# ENVIRONMENT VARIABLES END

# INITIALIZING COMPONENTS
data_adapter = get_data_adapter(data_path=DATA_PATH,
                                strategy=DATA_ADAPTER,
                                database_url=DATABASE_HOST,
                                database_port=DATABASE_PORT,
                                database_name=DATABASE_NAME)
socials = Socials()

while True:
    data = requests.get(RSS_FEED)
    content = json.loads(data.content)

    new_posts = data_adapter.add_and_get_new_items(items=content.get('items'))
    if len(new_posts) > 0:
        for i in new_posts:
            url = i.get('url') if i.get('url') is not None else ''
            summary = i.get('summary') if i.get('summary') is not None else \
                i.get('title') if i.get('title') is not None else ''
            socials.post('{}\n{}'.format(summary, url))

    time.sleep(REFRESH_TIME)
