FROM python:3.7.5-alpine3.10 

WORKDIR /root

COPY ./requirements.txt .

RUN pip install --upgrade pip \
  pip install -r requirements.txt

WORKDIR /discord_bot

ENV TOKEN={SERVER_TOKEN} \
  POST_CHANNEL_ID={POST_CHANNEL_ID}
