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
        message = cnt.const.IN + cnt.const.ENTERING_MESSAGE
        if(member.nick is None):
            message = cnt.const.CODEBLOCKS + message.replace('name', f'{str(member.name)}') + cnt.const.CODEBLOCKS
        else:
            message = cnt.const.CODEBLOCKS + message.replace('name', f'{str(member.nick)}') + cnt.const.CODEBLOCKS

    # 退室した場合
    # If someone left VOICE CHANNEL.
    elif(after.channel is None):
        message = cnt.const.OUT + cnt.const.LEAVING_MESSAGE
        if(member.nick is None):
            message = cnt.const.CODEBLOCKS + message.replace('name', f'{str(member.name)}') + cnt.const.CODEBLOCKS
        else:
            message = cnt.const.CODEBLOCKS + message.replace('name', f'{str(member.nick)}') + cnt.const.CODEBLOCKS

    return message

# 入退室管理
# Manage Entered and left.
@client.event
async def on_voice_state_update(member, before, after):
    message = ""
    # 発言するチャンネルの指定
    # Set channel id.
    channel = client.get_channel(int(os.environ['POST_CHANNEL_ID']))

    if(channel == ''):
        print('POST_CHANNEL_ID is empty')
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
