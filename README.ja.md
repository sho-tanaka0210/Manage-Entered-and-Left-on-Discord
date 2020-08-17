# DiscordのVC入退室通知ツール
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

このBOTを導入したDiscordサーバの  
ボイスチャットへIN or OUTした際のユーザ名を指定のチャンネルへ投稿します。

![Example](https://raw.github.com/wiki/mizukichi0210/Manage-Entered-and-Left-on-Discord/example_gif.gif)

ボイスチャットをしているメンバーが多く、誰が入ってきたのか、誰が出たのかが分からない！  
一々入りました、と伝えるのが面倒だ！という際に導入をしてみてはいかがでしょうか。

## 使用方法

使用方法としていくつかのパターンが存在します。  
今回手順として用意したパターン[heroku](#herokuでの運用)を用いるパターンと[ローカル実行](#ローカル実行での運用)の2つです。

### herokuでの運用

#### 前提

24時間常にBOTの稼働を続ける場合、herokuへクレジットカードの登録が必須になります。  
ただし、有料アドオンや他のアプリケーションを同時に運用しない限り無料枠へ収まりますので、  
下記手順の通りの実施であれば料金は発生しません。

料金に関する詳細は[公式ページ](https://jp.heroku.com/pricing)にてご確認ください。  
参考: 作成者が使用している70人規模のサーバであれば Free にて十分にカバーが可能です

### 導入手順

#### 前提
- GitHubアカウントを所持していること
- Herokuの承認済みアカウントを所持していること
- Discordのサーバ管理者権限
- Discordの開発者モード

上記の手順などは省略します。

#### 手順
Heroku CLIを用いる方法やContainer Registoryを用いたデプロイ方法があるのですが、  
以下ではGitHubリポジトリを用いた導入方法を記載します。

1. リポジトリをcloneする  
`git clone https://github.com/Mizukichi0210/Manage-Entered-and-Left-on-Discord.git`

2. 自分のアカウントに新しいリポジトリを作成する

Privateのリポジトリにすることを推奨します。

3. リモートリポジトリの情報を書き換えpushする

```bash
# git clone直後のリモートリポジトリの情報
$ git remote -v
origin  https://github.com/Mizukichi0210/Manage-Entered-and-Left-on-Discord.git (fetch)
origin  https://github.com/Mizukichi0210/Manage-Entered-and-Left-on-Discord.git (push)

# 新しく作成したリポジトリをoriginへ設定する
$ git remote set-url origin https://github.com/ユーザ名/リポジトリ名.git
$ git remote -v
origin  https://github.com/ユーザ名/リポジトリ名.git (fetch)
origin  https://github.com/ユーザ名/リポジトリ名.git (push)

# 新しく作成したリポジトリへpushする
$ git push origin -u master
Enumerating objects: 187, done.
Counting objects: 100% (187/187), done.
Delta compression using up to 16 threads
Compressing objects: 100% (126/126), done.
Writing objects: 100% (187/187), 34.71 KiB | 8.68 MiB/s, done.
Total 187 (delta 82), reused 134 (delta 55)
remote: Resolving deltas: 100% (82/82), done.
To https://github.com/ユーザ名/リポジトリ名.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
```

4. Heroku側でアプリの設定を行う

以下の手順に従えば設定が完了できる見込みです。

- [Heroku](https://id.heroku.com/login)へログイン
- [ダッシュボード - アプリ一覧](https://dashboard.heroku.com/apps)へ移動
- `New` -> `Create new app`を選択
- `App name`を記入
- `Choose a region`を選択後、`Create app`  
※ `United States`か`Europe`しかありませんのでどちらでも可です
- 以下の画像のように`Deployment method`とリポジトリを選択する

<img width="1281" alt="スクリーンショット 2020-06-03 3 02 55" src="https://user-images.githubusercontent.com/37664176/83553813-c0d99480-a546-11ea-92d6-30500db4eddd.png">

`App connected to GitHub`では、`Search`ボタンを押せば自分のリポジトリが表示されるはずです。  
そのため、2で作成した新しいリポジトリを選択してください。

5. 環境変数の設定

当BOTについて、実行の上でいくつかの環境変数の設定が必要です。

実行に必要な環境変数と概要は以下の通りです。

環境変数名 | 概要
:--: | :--:
POST_CHANNEL_ID | 入退室を投稿するチャンネルのID
TOKEN | BOTを起動するためのTOKEN

Herokuでの環境変数の設定方法

- `https://dashboard.heroku.com/apps/アプリ名/settings`へ移動
- `Config Vars`より上記の環境変数名(KEY)と必要な情報(VALUE)を追加する

以上で設定が完了です。

起動しない場合などはIssueを適当に作成していただけると...

### ローカル実行での運用

**非推奨**

#### 前提
- Dockerの導入

#### 使用方法
以下の手順で使用します。

```bash
# git clone
$ git clone git@github.com:Mizukichi0210/Manage-Entered-and-Left-on-Discord.git

$ cd Manage-Entered-and-Left-on-Discord

# Dockerファイルの ENV に必要な情報を設定すること
## 設定パラメータ
## {SERVER_TOKEN}: サーバのトークン
## {POST_CHANNEL_ID}: メッセージ投稿チャンネル

# 実行環境作成
$ docker build . -t bot-run-image

# 実行
$ docker run --rm --name bot-run-container -v $(pwd):/discord_bot -it bot-run-image /bin/ash
```

設定が正常に完了している場合、BOTがアクティブになり、
任意のボイスチャットへの入室 / 退出時に指定のチャンネルへメッセージが投稿されるようになります。

# 使用バージョン

時折更新します。

使用項目 | バージョン
-- | --
Python | 3.7.5
[discord.py](https://discordpy.readthedocs.io/ja/latest/) | 1.2.5

# Reference
[dockerで簡易にpython3の環境を作ってみる](https://qiita.com/reflet/items/4b3f91661a54ec70a7dc)

[Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

[Compose file version 3 reference](https://docs.docker.com/compose/compose-file/)

[Discordで通話時間を測定するBotを作ってみた](https://qiita.com/tokkq/items/311aa297175b9cf7f946)

# LICENSE
MIT