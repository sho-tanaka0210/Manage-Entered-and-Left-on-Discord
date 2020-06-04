# Regular posting of messages
[日本語](./README.ja.md)

NOTE: This README has been translated using DeepL.

It is a function to post messages periodically by BOT.  
If you want to use it, please make your own settings.

## Assumptions.
You need to set each time zone to run it.  
Set the user's time zone in the execution environment and set the time and day of the week in the user's time zone.

If you want to run it on Heroku, add the following data to `Config Vars` of `https://dashboard.heroku.com/apps/Application Name/settings`.

<img width="801" alt="Screenshot 2020-06-05 0 09 47" src="https://user-images.githubusercontent.com/37664176/83774606-dffc3180-a6c0-11ea-9303-50baacbf9cf7.png">

An example of notation is as follows
- America/Costa_Rica
- Asia/Sakhalin
- Antarctica/DumontDUrville

Please set a time zone for each one.

## How to use it.
Move two folders, `day_of_week_enum.py` and `post_day.py`, to the directory where `bot.py` is located.
2. add the following code to `bot.py`.

```python
# Ability to post recurring messages
@tasks.loop(seconds=60)
async def regular_message():
    channel = client.get_channel(int(os.environ['POST_CHANNEL_ID']))

    if(channel == ''). print('POST_CHANNEL_ID is empty'):
        print('POST_CHANNEL_ID is empty')
        return

    # Get the current time.
    now = datetime.now().strftime('%H:%M')
    Try. message = ''
        message = ''

        # Time to post the message.
        if(now == '10:00' or now == '19:00' or now == '23:00'):
            weekday = datetime.today().weekday()
            weekday_name = calendar.day_name[weekday]

            # Day of the week to post a message.
            if(weekday_name == 'Monday' or weekday_name == 'Wednesday'):
                message = cnt.const.POST_MESSAGE
                message = cnt.const.EVERYONE + cnt.const.SEPARATOR + message
        if(message == ''):
            return

        await channel.send(message)
        return
    Print(e)
        print(e)

# Activate the recurring message posting feature.
regular_message.start()
```
**I recommend that you keep your voice chat entry and exit messages separate from the channels you post them on. **

However, with the above code, the posts are to the same channel, so
please add an environment variable to support it

3. setting the time to post the message

`if(now == '10:00' or now == '19:00' or now == '23:00'):`   
Modify the above part.

It is possible to post in multiple time zones if you connect them with the form `now == HH:mm or now == HH:mm or ...`

4. setting the day of the week to post a message

`if(weekday_name == 'Monday' or weekday_name == 'Wednesday'):`  
You can configure it by modifying the above part.

It is possible to set multiple days of the week by connecting them with the following format: `weekday_name == 'Monday' or...`

This completes the setup.

If you restart the application, the settings may be reflected.

-----

Translated with www.DeepL.com/Translator (free version)
