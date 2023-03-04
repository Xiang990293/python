import pafy

url = "https://www.youtube.com/watch?v=jZN90LaVFXg"

video = pafy.new(url)

streams = video.streams
for i in streams:
    print(i)

best = video.getbest()
  
print(best.resolution, best.extension)
  
best.download()