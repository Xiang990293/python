from yt_dlp import YoutubeDL
import yt_dlp
import threading

url = "https://zh.wikipedia.org/wiki/Help:%E8%8B%B1%E8%AA%9E%E5%9C%8B%E9%9A%9B%E9%9F%B3%E6%A8%99"

def downl(url):
	with YoutubeDL() as ydl:
		info_dict = ydl.extract_info(url, download=True)
		filename = ydl.prepare_filename(info_dict)

	return filename, info_dict

def call(url):
	filename, info_dict = downl(url)
	return filename, info_dict
	
try:
	thread = threading.Thread(target=call, args=url)
	thread.start()
	print("success!")
except yt_dlp.utils.DownloadError:
	print("got you beach, DLE")
except yt_dlp.utils.ExtractorError:
	print("got you beach, EE")