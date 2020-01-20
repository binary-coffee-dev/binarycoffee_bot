# Binary Coffee Bot

**Telegram** bot that publishes the latest articles from our [blog](https://binary-coffee.dev) to our [Telegram channel](https://t.me/binarycoffeedev). If you have a blog and want to send the posts automatically to a telegram channel you can use this bot.

1. Clone ths repo: `git clone https://github.com/dcs-community/binarycoffee_bot.git`
2. Create enviroment: `virtualenv -p python3 env`
3. Activate enviroment: `source env/bin/activate`
4. Set enviroment variables:
    * `CHANNEL`: your channel user **@channel**
    * `TOKEN`: your bot token, you can see [this post](https://binary-coffee.dev/post/como-hacer-un-bot-de-telegram-desde-cero-con-python)
    * `RSS_FEED`: Url of a JSON Feed of your blog.
5. Finally run `python bot.py`

You can also deploy it to Heroku, see [this post](https://binary-coffee.dev/post/aprende-a-desplegar-un-bot-de-telegram-en-heroku) for help.
