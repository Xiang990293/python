import yt_dlp
import easygui as g
import os

while True:
	url = g.enterbox("請輸入影片網址", "影片下載器")
	if url == None:
		break

	with yt_dlp.YoutubeDL() as ydl:
		result = ydl.download(url)
