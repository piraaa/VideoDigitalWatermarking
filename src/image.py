#
# image.py
# Created by pira on 2017/07/28.
#

#coding: utf-8

import numpy as np
import cv2

def readImage(filename):
	#imreadのflags flags>0(cv2.IMREAD_COLOR):3ChannelColors,flags=0(cv2.IMREAD_GRAYSCALE):GrayScale,flags<0(cv2.IMREAD_UNCHANGED):Original
	#白黒画像でも強制的にRGBで扱う．
	img = cv2.imread(filename, 1)
	print('Read ' + filename + '.')
	return img

def writeImage(filename, img):
	cv2.imwrite(filename, img)
	print('Write '+filename+'.')

def printImage(img):
	cv2.imshow('Image', img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()