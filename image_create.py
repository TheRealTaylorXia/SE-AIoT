import cv2 as cv
import numpy as np
import os
import sys

dirs = os.listdir("negatives/")
num = 1

def gray_n_resize():
    for images in dirs:
        img = cv.imread("negatives/"+images+".jpeg",cv.IMREAD_ANYDEPTH)
        cv.imshow("image",img)
        mat gray_image
        cvt(image, gray_image,CV_BGR2GRAY)
        #res = cv.resize(img, (300,300))
        #cv.imwrite("neg/"+str(num)+".jpeg", res)
        #num += 1

gray_n_resize()
