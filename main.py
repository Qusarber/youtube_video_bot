from pytube import YouTube
import os


def video_quality(videourl):

    yt = YouTube(videourl)
    res = [stream.resolution for stream in yt.streams.filter(file_extension='mp4')]
    res = list(set(list(filter(None, res))))
    non_interested_res = ['144p', '240p', '360p', '480p']
    for i in non_interested_res:
        if i in res:
            res.remove(i)
    res.sort(key=lambda x: int(x.split('p')[0]))
    return res


def video_downloader(videourl, videoquality):

    yt = YouTube(videourl)
    path = yt.title
    try:
        yt = yt.streams.filter(res=f"{videoquality}", file_extension='mp4').desc().first()
        if not os.path.exists(path):
            os.makedirs(path)
        yt.download(path)
    except:
        yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        if not os.path.exists(path):
            os.makedirs(path)
        yt.download(path)

    return path, yt.default_filename
