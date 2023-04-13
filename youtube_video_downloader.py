import yt_dlp as youtube_dl
import pygame as pyg

url = "https://clips.twitch.tv/OriginalCourageousLatteUncleNox-Wpk9vcq8hoOvHC63"

with youtube_dl.YoutubeDL() as ydl:
    result = ydl.download(url)
