# youtube_video_bot
This Telegram bot can download video from youtube

At the moment, the bot can download videos up to 50 mb, future update will be asap.

If you have problems with pytube like this "could not find match for ^\w+\W":
in ur virtual env find cipher.py file and replace the line 30, which is:
```
var_regex = re.compile(r"^\w+\W")
```
With that line:
```
var_regex = re.compile(r"^\$*\w+\W"
```
