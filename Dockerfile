FROM python:3.7.5-alpine3.10 

RUN pip install --upgrade pip \
  setuptools && pip install multidict==4.5.2 \
  yarl==1.3.0

RUN mkdir -p discrod_bot
WORKDIR /discord_bot

# Install discord.py
RUN python3 -m pip install -U discord.py
