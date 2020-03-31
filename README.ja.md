# DiscordのVC入退室通知ツール

# バージョン

使用項目 | バージョン
-- | --
Python | 3.7.5
[discord.py](https://discordpy.readthedocs.io/ja/latest/) | 1.2.5

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

# 実行環境作成
$ docker build . -t bot-run-image

# 実行
$ docker run --rm --name bot-run-container -v $(pwd):/discord_bot -it bot-run-image /bin/ash
```

### デプロイの準備
**環境変数の設定**

1. `https://dashboard.heroku.com/apps/{APP_NAME}/settings` へ遷移
1. `Reveal Config Vars` の押下
1. `TOKEN` の設定
1. `MAIN_CHANNEL_ID` の設定
1. `KOKUCHI_CHANNEL_ID` の設定

上記手順で動作的に問題がないことが確認できた場合、  
herokuにて実際に使用を開始してください。

herokuへのデプロイ方法は[公式サイト](https://jp.heroku.com/home)参照のこと

良いVCライフを！

# Reference
[dockerで簡易にpython3の環境を作ってみる](https://qiita.com/reflet/items/4b3f91661a54ec70a7dc)

[Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

[Compose file version 3 reference](https://docs.docker.com/compose/compose-file/)

[Discordで通話時間を測定するBotを作ってみた](https://qiita.com/tokkq/items/311aa297175b9cf7f946)

# LICENSE
MIT