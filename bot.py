from env import CHANNEL, REFRESH_TIME
import telegram
import os
import time
import requests
import json

def load():
    file = open('data.json', 'r')
    data = file.read().replace("'", '"')
    ret = []
    if len(data) > 0:
        ret = json.loads(data)
    file.close()
    return ret

last_posts = load()

def save():
    with open('data.json', 'w+') as database:
        database.write(str(last_posts))

def send(msg, chat_id=CHANNEL, token=os.environ['TOKEN']):
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=msg)

while True:
    try:
        data = requests.get(os.environ['RSS_FEED'])
        posts = json.loads(data._content)
        
        if last_posts == []:
            for i in posts['items']:
                send('{}\n{}'.format(i['summary'], i['url']))
        
        elif posts != last_posts:
            for i in posts['items']:
                if i not in last_posts['items']:
                    send('{}\n{}'.format(i['summary'], i['url']))
        
        if posts != last_posts:
            last_posts = posts
            save()
    except:
        pass
    time.sleep(REFRESH_TIME)
