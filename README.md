# youtube_video_bot
Non-Commercial use only!

This Telegram bot can download video from youtube

In this version, you can manually select the available video quality (720p-2160p).
If errors occur, bot will try to download a 720p video.

Don't forger to set ur bot token in bot.py file

To run bot use:
```
python bot.py
```

Bot can download video under 50 mb size. If size is bigger, bot can send it to user with using userbot.
To use this feature you need configure your userbot with app api_id and app api_hash in userbot.py

You can create your app via https://my.telegram.org/apps

If you have problems with pytube like this "could not find match for ^\w+\W" do the next steps - 
in your virtual env find cipher.py file and replace the line 30, which is:
```
var_regex = re.compile(r"^\w+\W")
```
With that line:
```
var_regex = re.compile(r"^\$*\w+\W"
```
