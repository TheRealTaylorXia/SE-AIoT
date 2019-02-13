import cv2 as cv
from glob import glob


num = 1

def gray_n_resize():
    for filename in glob("neg/*"):
        o_img = cv.imread(filename, cv.IMREAD_UNCHANGED)
	g_img = cv.cvtColor(o_img, cv.COLOR_BGR2GRAY)
        img  = cv.resize(g_img, (300,300))
        cv.imwrite("negative/"+str(num)+'.jpg', img)
        num += 1

def create_bg():
	for filename in glob("negative/*"):
		line = filename+'\n'
		with open('bg.txt','a') as f:
			f.write(line)

#gray_n_resize()
#create_bg
