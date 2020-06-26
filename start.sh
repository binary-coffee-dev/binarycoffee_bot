#!/usr/bin/env bash

if [ -f .env ]
then
  export $(cat .env | xargs)
fi

python3 bot.py
