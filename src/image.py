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
	print('Read "' + filename + '".')
	return img

def writeImage(filename, img):
	cv2.imwrite(filename, img)
	print('Write "'+filename+'".')

def printImage(img):
	cv2.imshow('Image', img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def rgb2ycc(img):
	u"""RGB to YCbCr.
	@param  img     :3 dimension np.ndarray[Height][Width][RGB]
	@return ycc_data:3 dimension np.ndarray[Height][Width][YCC]
	"""
	height = img.shape[0]
	width  = img.shape[1]
	ycc_data = np.empty([height,width,3])
	for i in np.arange(height):
		for j in np.arange(width):
			ycc_data[i][j][0] =  0.299*img[i][j][2] + 0.587*img[i][j][1] + 0.114*img[i][j][0] #Y
			ycc_data[i][j][1] = -0.169*img[i][j][2] - 0.331*img[i][j][1] + 0.500*img[i][j][0] #Cb
			ycc_data[i][j][2] =  0.500*img[i][j][2] - 0.419*img[i][j][1] - 0.081*img[i][j][0] #Cr
	return ycc_data

def ycc2rgb(img):
	u"""YCbCr to BGR.
	@param  img     :3 dimension np.ndarray[Height][Width][YCC]
	@return rgb_data:3 dimension np.ndarray[Height][Width][BGR]
	"""
	height = img.shape[0]
	width  = img.shape[1]
	rgb_data = np.empty([height,width,3])
	for i in np.arange(height):
		for j in np.arange(width):
			rgb_data[i][j][0] = img[i][j][0] + 1.772*img[i][j][1] #B
			rgb_data[i][j][1] = img[i][j][0] - 0.344*img[i][j][1] - 0.714*img[i][j][2] #G
			rgb_data[i][j][2] = img[i][j][0] + 1.402*img[i][j][2] #R
	return rgb_data
