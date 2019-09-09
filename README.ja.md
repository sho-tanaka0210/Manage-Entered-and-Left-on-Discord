# DiscordのVC入退室通知ツール

# バージョン

使用項目 | バージョン
-- | --
Python | 3.6
[discord.py](https://discordpy.readthedocs.io/ja/latest/) | 1.2.0a

# 使用

このプログラムはherokuでの運用を想定しています。  
ソースコードをcloneしてお使いください。

## 使用方法

```bash
# git clone
$ git clone git@github.com:Mizukichi0210/Manage-Entered-and-Left-on-Discord.git

$ cd Manage-Entered-and-Left-on-Discord

# config.iniの作成
# tokenとchannel_idを設定する
$ cp -p config_example.ini config.ini

# テスト実行
$ docker-compose up -d --build
$ docker-compose run --rm bot python bot.py

# コンテナの停止
$ docker-compose down
```

上記手順で動作的に問題がないことが確認できた場合、  
herokuにて実際に使用を開始してください。

# Reference
[dockerで簡易にpython3の環境を作ってみる](https://qiita.com/reflet/items/4b3f91661a54ec70a7dc)

[Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

[Compose file version 3 reference](https://docs.docker.com/compose/compose-file/)

[Discordで通話時間を測定するBotを作ってみた](https://qiita.com/tokkq/items/311aa297175b9cf7f946)

# LICENSE
MIT