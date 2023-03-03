import cv2 
import os
import gzip

# video = cv2.VideoCapture('bad_apple_ingredients/bad_apple.mp4')
# try:
# 	if not os.path.exists('bad_apple_output'):
# 		os.makedirs('bad_apple_output')
# except OSError:
# 	print ('Error')
# currentframe = 0
# while(True):
# 	ret,frame = video.read()

# 	if ret:
# 		name = 'bad_apple_output/' + str(currentframe) + '.jpg'
# 		print ('Captured...' + name)
# 		cv2.imwrite(name, frame)
# 		currentframe += 1
# 	else:
# 		break
# video.release()
# cv2.destroyAllWindows()

with gzip.open('bad_apple_ingredients/test_0.nbt', 'r+b') as f, gzip.open('bad_apple_ingredients/test_1.nbt', 'rb') as g:
    # with open('bad_apple_output/output.txt','r+') as txt:
    #     print(f.read(), file=t.xt)

    # with open('bad_apple_output/output2.txt','r+') as txt:
    #     print(g.read(), file=txt)
    with gzip.open('bad_apple_output/output_nbt.nbt','wb+') as nbt:
        nbt.write(f.read())