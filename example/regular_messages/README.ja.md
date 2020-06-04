# メッセージの定期投稿

BOTによるメッセージの定期投稿の機能です。  
使用したい方は各自で設定を行ってください。

## 前提
実行するためには各々のタイムゾーンの設定が必要です。  
使用者のタイムゾーンを実行環境にて設定し、使用者のタイムゾーンの時刻や曜日で設定を行ってください。

Herokuでの実行を想定している場合、 `https://dashboard.heroku.com/apps/アプリ名/settings` の `Config Vars` に以下のようなデータを追加してください。

<img width="801" alt="スクリーンショット 2020-06-05 0 09 47" src="https://user-images.githubusercontent.com/37664176/83774606-dffc3180-a6c0-11ea-9303-50baacbf9cf7.png">

表記例としては以下の通りです。
- America/Costa_Rica
- Asia/Sakhalin
- Antarctica/DumontDUrville

各々のタイムゾーンの設定をお願いします。

## 使い方
1. `day_of_week_enum.py` と `post_day.py` の2つのフォルダを `bot.py` がある階層まで移動させる
2. `bot.py` に次のコードを付け加える

```python
# 定期的なメッセージ投稿機能
@tasks.loop(seconds=60)
async def regular_message():
    channel = client.get_channel(int(os.environ['POST_CHANNEL_ID']))

    if(channel == ''):
        print('POST_CHANNEL_ID is empty')
        return

    # 現在の時刻を取得
    now = datetime.now().strftime('%H:%M')
    try:
        message = ''

        # メッセージ投稿時刻
        if(now == '10:00' or now == '19:00' or now == '23:00'):
            weekday = datetime.today().weekday()
            weekday_name = calendar.day_name[weekday]

            # メッセージ投稿曜日
            if(weekday_name == 'Monday' or weekday_name == 'Wednesday'):
                message = cnt.const.POST_MESSAGE
                message = cnt.const.EVERYONE + cnt.const.SEPARATOR + message
        if(message == ''):
            return

        await channel.send(message)
        return
    except Exception as e:
        print(e)

# 定期的なメッセージの投稿機能のアクティベート
regular_message.start()
```

**ボイスチャット入退室のメッセージを投稿するチャンネルとは別にすることを推奨します。**

ただし上記のコードでは同一のチャンネルへの投稿となっているため、
環境変数を追加し対応をしてください。

3. メッセージを投稿する時刻の設定

`if(now == '10:00' or now == '19:00' or now == '23:00'):`   
上記の部分を変更する。

`now == HH:mm or now == HH:mm or ...`　という形式でつなげていけば複数の時間帯での投稿が可能です。

4. メッセージを投稿する曜日の設定

`if(weekday_name == 'Monday' or weekday_name == 'Wednesday'):`  
上記の部分を変更することで設定できます。

`weekday_name == 'Monday' or...` という形式でつなげていくことで複数の曜日での設定が可能です。

以上で設定が完了です。

アプリケーションを再起動をすると設定が反映されるかと思います。
