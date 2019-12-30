import discord
import configparser
import re
import random
import calendar
import constants as cnt

from discord.ext import tasks
from datetime import datetime 

print(cnt.const.RUN_MESSAGE)

client = discord.Client()

# config.ini の読み込み
# Read config.ini
inifile = configparser.ConfigParser()
inifile.read('./config.ini', 'UTF-8')

# 定期的なメッセージ投稿機能
# Message posting function at specified time
@tasks.loop(seconds=60)
async def loop():
    channel = ''
    if(str(inifile.get('application_environment', 'env')) == 'prod'):
        channel = client.get_channel(int(inifile.get('bot_settings', 'main_channel_id')))
    elif(str(inifile.get('application_environment', 'env')) == 'test'):
        channel = client.get_channel(int(inifile.get('bot_settings', 'channel_id_test')))

    if(channel == ''):
        print('main_channel_idが空です')
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
# If you want to use message posting function at specified time, remove comment out.
# loop.start()

# 入退室管理
# Manage Entered and left.
@client.event
async def on_voice_state_update(member, before, after):
    message = ""
    # 発言するチャンネルの指定
    # Set channel id.
    channel = ''
    if(str(inifile.get('application_environment', 'env')) == 'prod'):
        channel = client.get_channel(int(inifile.get('bot_settings', 'kokuchi_channel_id')))
    elif(str(inifile.get('application_environment', 'env')) == 'test'):
        channel = client.get_channel(int(inifile.get('bot_settings', 'channel_id_test')))

    try:
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

        # メッセージがIN or OUTのみの場合は何もしない
        # Do nothing if message has only [IN] or [OUT].
        if (len(message) == len(cnt.const.IN) or len(message) == len(cnt.const.OUT) or message == ''):
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
if(str(inifile.get('application_environment', 'env')) == 'prod'):
    client.run(inifile.get('bot_settings','token'))
elif(str(inifile.get('application_environment', 'env')) == 'test'):
    client.run(inifile.get('bot_settings','token_test'))
