#
# image.py
# Created by pira on 2017/07/28.
#

#coding: utf-8
u"""For image processing."""

import sys
import numpy as np
import cv2

RED   = 2
GREEN = 1
BLUE  = 0

def readGrayImage(filename):
	u"""Read grayscale image.
	@param  filename : filename
	@return img      : 2 dimension np.ndarray[Height][Width]
	"""
	#imread flags=0(cv2.IMREAD_GRAYSCALE):GrayScale
	img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
	#print('Read "' + filename + '".')
	return img

def readColorImage(filename):
	u"""Read color image. [notice] Grayscale images are treated as RGB image. (ex. if pixel value is 100, it's treated [100][100][100] RGB image.)
	@param  filename : filename
	@return img      : 3 dimension np.ndarray[Height][Width][BGR]
	"""
	#imread flags>0(cv2.IMREAD_COLOR):3ChannelColors
	#白黒画像でも強制的にRGBで扱ってしまう．
	img = cv2.imread(filename, cv2.IMREAD_COLOR)
	#print('Read "' + filename + '".')
	return img

def getRgbLayer(img, rgb=RED):
	u"""Read grayscale image.
	@param  img   : a 3 dimension color image like np.ndarray[Height][Width][BGR]
	@param  rgb   : a returned layer number. Blue is 0, Green is 1 and Red is 2. You can also give a colorname like RED.  
	@return layer : a color layer of image, only red, green or blue.
	"""
	height = img.shape[0]
	width  = img.shape[1]
	layer = np.empty([height, width])

	for i in np.arange(height):
		for j in np.arange(width):
			layer[i][j] = img[i][j][rgb]

	return layer

def writeImage(filename, img):
	u"""Export image data.
	@param filename : filename for export image data
	@param img      : 2 or 3 dimension image array
	"""
	cv2.imwrite(filename, img)
	#print('Write "'+filename+'".')

def showImage(img):
	u"""Show imsge data.
	@param img : image array
	"""
	cv2.imshow('Image', img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def grayimage2block(img, size):
	u"""Divide gray image into blocks.
	@param  img    : a 2 dimension gray image like a np.array[height][width]
	@param  size   : block size list like a [height, width]
	@return blocks : a 4 dimension blocks like a np.ndarray[block_height][block_width][height][width]
	"""
	image_height = int(img.shape[0])
	image_width  = int(img.shape[1])
	block_height = int(size[0])
	block_width  = int(size[1])

	#print(image_height, image_width, block_height, block_width)

	if image_height%block_height != 0 or image_width%block_width != 0:
		print('Please give an appropriate bloxk size.')
		print('You can use only numbers that are divisors of image height and width as block size.')
		sys.exit()

	row = int(image_height / block_height)
	col = int(image_width  / block_width)
	blocks = np.empty([row, col, block_height, block_width])
	#print('blocks shape =', blocks.shape)

	for i in np.arange(row):
		for j in np.arange(col):
			for k in np.arange(block_height):
				for l in np.arange(block_width):
					blocks[i][j][k][l] = img[i*block_height+k][j*block_width+l]

	return blocks

def colorimage2block(img, size):
	u"""Divide color image into blocks.
	@param  img    : a 3 dimension image like a np.array[height][width][BGR]
	@param  size   : block size list like a [height, width]
	@return blocks : a 5 dimension blocks like a np.ndarray[block_height][block_width][height][width][BGR]
	"""
	image_height = int(img.shape[0])
	image_width  = int(img.shape[1])
	block_height = int(size[0])
	block_width  = int(size[1])
	color_num = int(img.shape[2])

	#print(image_height, image_width, block_height, block_width)

	if image_height%block_height != 0 or image_width%block_width != 0:
		print('Please give an appropriate bloxk size.')
		print('You can use only numbers that are divisors of image height and width as block size.')
		sys.exit()

	row = int(image_height / block_height)
	col = int(image_width  / block_width)
	blocks = np.empty([row, col, block_height, block_width, color_num])
	
	#print('blocks shape =', blocks.shape)

	for i in np.arange(row):
		for j in np.arange(col):
			for k in np.arange(block_height):
				for l in np.arange(block_width):
						for rgb in np.arange(color_num):
							blocks[i][j][k][l][rgb] = img[i*block_height+k][j*block_width+l][rgb]

	return blocks

def rgb2ycc(img):
	u"""RGB to YCbCr.
	@param  img      : 3 dimension np.ndarray[Height][Width][RGB]
	@return ycc_data : 3 dimension np.ndarray[Height][Width][YCC]
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
	@param  img      : 3 dimension np.ndarray[Height][Width][YCC]
	@return rgb_data : 3 dimension np.ndarray[Height][Width][BGR]
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
	@param  img     : 3 dimension np.ndarray[Height][Width][YCC]
	@return y_data  : 2 dimension np.ndarray[Height][Width]. Including only Y.
	"""
	height = img.shape[0]
	width  = img.shape[1]
	y_data = np.empty([height,width])
	for i in np.arange(height):
		for j in np.arange(width):
			y_data[i][j] = img[i][j][0]
	return y_data

