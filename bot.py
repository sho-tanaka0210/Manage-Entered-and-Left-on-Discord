import calendar
import configparser
import constants as cnt
import discord
import os
import re
import random

from discord.ext import tasks
from datetime import datetime 

print(cnt.const.RUN_MESSAGE)

client = discord.Client()

# config.ini の読み込み
# Read config.ini
inifile = configparser.ConfigParser()
inifile.read('./config.ini', 'UTF-8')

async def create_code_block_message(member, before, after):
    """Create a message with codeblock
    :param
        - member: Logged in / logged out user
        - before: Is started voice chat
        - after: Is left voice chat
    """
    message = ''
    # 入室した場合
    # If someone enterd VOICE CHANNEL.
    if(before.channel is None):
        message = cnt.const.IN + inifile.get('entering_message', str(random.randrange(8)))
        if(member.nick is None):
            message = cnt.const.CODEBLOCKS + message.replace('name', f'{str(member.name)}') + cnt.const.CODEBLOCKS
        else:
            message = cnt.const.CODEBLOCKS + message.replace('name', f'{str(member.nick)}') + cnt.const.CODEBLOCKS

    # 退室した場合
    # If someone left VOICE CHANNEL.
    elif(after.channel is None):
        message = cnt.const.OUT + inifile.get('leaving_message', str(random.randrange(7)))
        if(member.nick is None):
            message = cnt.const.CODEBLOCKS + message.replace('name', f'{str(member.name)}') + cnt.const.CODEBLOCKS
        else:
            message = cnt.const.CODEBLOCKS + message.replace('name', f'{str(member.nick)}') + cnt.const.CODEBLOCKS

    return message

# 定期的なメッセージ投稿機能
# Message posting function at specified time
@tasks.loop(seconds=60)
async def loop():
    channel = client.get_channel(int(os.environ['MAIN_CHANNEL_ID']))

    if(channel == ''):
        print('MAIN_CHANNEL_ID is empty')
        return

    # 現在の時刻を取得
    # Get current time
    now = datetime.now().strftime('%H:%M')
    try:
        message = ''
        # TODO: 将来的にlistで持てるようにする
        # メッセージ投稿時刻
        # Message posting time
        if(now == '10:00' or now == '19:00' or now == '23:00'):
            weekday = datetime.today().weekday()
            weekday_name = calendar.day_name[weekday]
            # TODO: 将来的にlistで持てるようにする
            # メッセージ投稿曜日
            # Message posting day
            if(weekday_name == 'Monday' or weekday_name == 'Wednesday'):
                message = cnt.const.POST_MESSAGE
                message = cnt.const.EVERYONE + cnt.const.SEPARATOR + message
        if(message == ''):
            return
        print(message)
        await channel.send(message)
        return
    except Exception as e:
        print(e)

# 定期的なメッセージ投稿を使用した場合、コメントアウトを消すこと
# If you want to use message posting function at specified time, 
# remove comment out.
# loop.start()

# 入退室管理
# Manage Entered and left.
@client.event
async def on_voice_state_update(member, before, after):
    message = ""
    # 発言するチャンネルの指定
    # Set channel id.
    channel = client.get_channel(int(os.environ['KOKUCHI_CHANNEL_ID']))

    if(channel == ''):
        print('KOKUCHI_CHANNEL_ID is empty')
        return

    try:
        # 入室した場合
        # If someone enterd VOICE CHANNEL.
        message = await create_code_block_message(member, before, after)

        # メッセージがIN or OUTのみの場合は何もしない
        # Do nothing if message has only [IN] or [OUT].
        if (len(message) == len(cnt.const.IN) or 
                len(message) == len(cnt.const.OUT) or message == ''):
            return
        print(message.replace(cnt.const.CODEBLOCKS, ''))
        await channel.send(message)
        return

    except Exception as e:
        # TODO: 例外の扱いについて考える
        # TODO: How to handle exception output.
        print(e)

# botの接続と起動
# Set token.
client.run(os.environ['TOKEN'])
