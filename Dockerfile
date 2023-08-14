FROM python:3.7-alpine

RUN apk add --no-cache --virtual .build-deps \
    ca-certificates gcc postgresql-dev linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev

WORKDIR /home/
COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY utils ./utils
COPY bot.py .env start.sh ./

CMD ["/bin/sh", "start.sh"]
