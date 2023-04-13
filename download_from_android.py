from bs4 import BeautifulSoup
import urllib.request
import re

html_page = "https://Xiang990293.github.io/home.html"
req = urllib.request.Request(html_page)
web = urllib.request.urlopen(req)
html = web.read()

soup = BeautifulSoup(html, "html.parser")

for link in soup.findAll('a'):
	print(link.get('href'))
	print("\n")