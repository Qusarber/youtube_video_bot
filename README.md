# youtube_video_bot
This Telegram bot can download video from youtube

Don't forger to set ur bot token in bot.py file

To run bot use:
```
python bot.py
```

Bot can download video under 50 mb size. If size if bigger bot can save it into your saved messages using userbot.
To use this feature you need configure your userbot with api_id and api_hash in userbot.py

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
