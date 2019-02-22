import cv2 as cv
import numpy as np
import os
import glob


path = "negatives/"
#path = "positives/"

folder = "neg/"
#folder = "pos/"

dirs = os.listdir(path)
num = 1

CWD = os.getcwd()

def gray_n_resize():
    for name in glob.glob(CWD+path+'/*'):
        img = cv.imread(name, cv.IMREAD_GRAYSCALE)
        res = cv.resize(img, (300, 300))
        cv.imwrite(folder + str(num) + '.jpg', res)
        num += 1

gray_n_resize()
