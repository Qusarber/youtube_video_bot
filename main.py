from pytube import YouTube
import os

def video_downloader(videourl):

    yt = YouTube(videourl)
    path = yt.title
    try:
        yt = yt.streams.filter(res="2160p").first()
    except:
        try:
            yt = yt.streams.filter(res="1440p").first()
        except:
            yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    yt.download(path)
    
    return path, yt.default_filename
