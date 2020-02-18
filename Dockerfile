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
ARG REFRESH_TIME
ARG DATA_ADAPTER

ENV CHANNEL=${CHANNEL}
ENV TOKEN=${TOKEN}
ENV RSS_FEED=${RSS_FEED}
ENV REFRESH_TIME=${REFRESH_TIME}
ENV DATA_ADAPTER=${DATA_ADAPTER}

CMD ["python", "bot.py"]
