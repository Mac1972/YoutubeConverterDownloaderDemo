from pytube import YouTube

link= '.............'
yt=YouTube(link)
video=yt.streams.filter(file_extension='mp4', res='144p').first()
video.download()

