# Notification for entered and left on Discord

[日本語](./README.ja.md)

# Version

Item | version
-- | --
Python | 3.7.5
[discord.py](https://discordpy.readthedocs.io/en/latest/) | 1.2.5

# Usage

This program assumes operation with heroku.  
Please clone the source code.

## How to use

```bash
# git clone
$ git clone git@github.com:Mizukichi0210/Manage-Entered-and-Left-on-Discord.git

$ cd Manage-Entered-and-Left-on-Discord

# Create config.ini
# Set token and channel id
$ cp -p config_example.ini config.ini

# Generate docker image
$ docker build . -t bot-run-image

# Run
$ docker run --rm --name bot-run-container -v $(pwd):/discord_bot -it bot-run-image /bin/ash
```

If you ’ve verified that your program is working correctly with the steps above,  
Please start using it on heroku.

# Reference
[dockerで簡易にpython3の環境を作ってみる](https://qiita.com/reflet/items/4b3f91661a54ec70a7dc)

[Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

[Compose file version 3 reference](https://docs.docker.com/compose/compose-file/)

[Discordで通話時間を測定するBotを作ってみた](https://qiita.com/tokkq/items/311aa297175b9cf7f946)

# LICENSE
MIT