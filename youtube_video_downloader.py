import yt_dlp as youtube_dl

url = "https://www.youtube.com/watch?v=jZN90LaVFXg"

with youtube_dl.YoutubeDL() as ydl:
    result = ydl.download(url)
