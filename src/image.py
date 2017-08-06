#
# image.py
# Created by pira on 2017/07/28.
#

#coding: utf-8
u"""For image processing."""

import numpy as np
import cv2

def readGrayImage(filename):
	u"""Read grayscale image.
	@param  filename:filename
	@return img     :2 dimension np.ndarray[Height][Width]
	"""
	#imread flags=0(cv2.IMREAD_GRAYSCALE):GrayScale
	img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
	print('Read "' + filename + '".')
	return img

def readColorImage(filename):
	u"""Read color image.
	[notice] Grayscale images are treated as RGB image. 
	         (ex. if pixel value is 100, it's treated [100][100][100] RGB image.)
	@param  filename:filename
	@return img     :3 dimension np.ndarray[Height][Width][BGR]
	"""
	#imread flags>0(cv2.IMREAD_COLOR):3ChannelColors
	#白黒画像でも強制的にRGBで扱ってしまう．
	img = cv2.imread(filename, cv2.IMREAD_COLOR)
	print('Read "' + filename + '".')
	return img

def writeImage(filename, img):
	cv2.imwrite(filename, img)
	print('Write "'+filename+'".')

def showImage(img):
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

def get_y(img):
	u"""Get only Y from YCC image.
	@param  img    :3 dimension np.ndarray[Height][Width][YCC]
	@return y_data :2 dimension np.ndarray[Height][Width]. Including only Y.
	"""
	height = img.shape[0]
	width  = img.shape[1]
	y_data = np.empty([height,width])
	for i in np.arange(height):
		for j in np.arange(width):
			y_data[i][j] = img[i][j][0]
	return y_data

