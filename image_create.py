import cv2 as cv
import numpy as np
import os
import sys

dirs = os.listdir("negatives/")
num = 1

def gray_n_resize():
    for name in glob.glob.glob(CWD + path + '/*'):
        img = cv.imread(name, cv.IMREAD_GRAYSCALE)
        res = cv.resize(img, (300, 300))
        cv.imwrite(folder + str(num) + '.jpg', res)
        num += 1

def create_bg():
	for filename in glob.glob("negative/*"):
		line = filename+'\n'
		with open('bg.txt','a') as f:
			f.write(line)


gray_n_resize()
#create_bg
