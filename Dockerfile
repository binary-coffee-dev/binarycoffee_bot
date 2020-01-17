FROM python:3

WORKDIR /bynarycoffee_bot

COPY requirements.txt /bynarycoffee_bot

RUN pip install -r requirements.txt

COPY . /bynarycoffee_bot

RUN touch data.json

CMD [ "python", "./bot.py" ]
