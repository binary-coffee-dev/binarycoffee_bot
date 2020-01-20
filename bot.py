from social import Telegram, Facebook
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
facebook_page = Facebook()

def post(msg):
    telegram_channel.post(msg)    
    facebook_page.post(msg)

while True:
    try:
        data = requests.get(os.environ['RSS_FEED'])
        posts = json.loads(data._content)
        
        if last_posts == []:
            for i in posts['items']:
                post('{}\n{}'.format(i['summary'], i['url']))
        
        elif posts != last_posts:
            for i in posts['items']:
                if i not in last_posts['items']:
                    post('{}\n{}'.format(i['summary'], i['url']))
        
        if posts != last_posts:
            last_posts = posts
            save()
    except:
        pass
    
    time.sleep(REFRESH_TIME)
