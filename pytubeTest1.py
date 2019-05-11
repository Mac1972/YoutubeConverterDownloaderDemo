from pytube import YouTube

link= 'https://www.youtube.com/watch?v=qmVsOat4YF8'
yt=YouTube(link)
video=yt.streams.filter(file_extension='mp4', res='1080p').first()
video.download()

