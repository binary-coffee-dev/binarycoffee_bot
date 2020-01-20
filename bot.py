from social import Telegram
import os
import time
import requests
import json

REFRESH_TIME = 60

def load_data():
    file = open('data.json', 'r')
    data = file.read().replace("'", '"')
    ret = []
    if len(data) > 0:
        ret = json.loads(data)
    file.close()
    return ret

def save():
    with open('data.json', 'w+') as database:
        database.write(str(last_posts))

last_posts = load_data()
telegram_channel = Telegram()

while True:
    try:
        data = requests.get(os.environ['RSS_FEED'])
        posts = json.loads(data._content)
        
        if last_posts == []:
            for i in posts['items']:
                telegram_channel.post('{}\n{}'.format(i['summary'], i['url']))
        
        elif posts != last_posts:
            for i in posts['items']:
                if i not in last_posts['items']:
                    telegram_channel.post('{}\n{}'.format(i['summary'], i['url']))
        
        if posts != last_posts:
            last_posts = posts
            save()
    except:
        pass
    
    time.sleep(REFRESH_TIME)
