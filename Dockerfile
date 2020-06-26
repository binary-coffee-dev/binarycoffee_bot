FROM python:3.6.0-alpine

RUN apk add --no-cache --virtual .build-deps \
    ca-certificates gcc postgresql-dev linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev

ADD requirements.txt /home/
WORKDIR /home/
RUN pip install -r requirements.txt

ADD . /home/

ARG CHANNEL
ARG TOKEN
ARG RSS_FEED

ENV CHANNEL=${CHANNEL}
ENV TOKEN=${TOKEN}
ENV RSS_FEED=${RSS_FEED}

CMD ["python", "bot.py"]
