import discord
import configparser
import re

client = discord.Client()

# config.ini の読み込み
# Read config.ini
inifile = configparser.ConfigParser()
inifile.read('./resources/config.ini', 'UTF-8')

# 改行コードの設定
# Set separator
SEPARATOR = "\n"

#  '!help'コマンドが入力された場合
# If someone entered '!help'.
@client.event
async def on_message(message):
	if message.content.startswith('!help'):
		text = inifile.get('message','help_message_1') + SEPARATOR + inifile.get('message','help_message_2')
		await client.send_message(message.channel, text)

# 入退室管理
# Manage Entered and left.
@client.event
async def on_voice_state_update(before, after):
	player_name = ""
	text = ""

	channel_name = inifile.get('bot_settings', 'channel_name')

	# config.ini へ記載したチャンネル名と一致した場合
	if(channel_name == str(before.voice_channel)
			or channel_name == str(after.voice_channel)):

		# 入室した場合
		# If someone enterd VOICE CHANNEL.
		if(before.voice_channel is None):
			player_name = after.name
			text = player_name + inifile.get('message','entering_message')

		# 退室した場合
		# If someone left VOICE CHANNEL.
		elif(after.voice_channel is None):
			player_name = before.name
			text = player_name + inifile.get('message','leaving_message')

		# 発言するチャンネルの指定
		# Set channel id.
		channel = client.get_channel(inifile.get('bot_settings','channel_id'))
		await client.send_message(channel, text)

# botの接続と起動
# Set token.
client.run(inifile.get('bot_settings','token'))