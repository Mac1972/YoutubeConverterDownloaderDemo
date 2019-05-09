from pytube import YouTube

link= '.............'
yt=YouTube(link)
video=yt.streams.filter(file_extension='mp4', res='1080p').first()
video.download()

