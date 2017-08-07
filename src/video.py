#
# video.py
# Created by pira on 2017/07/31.
#

#coding: utf-8
u"""For video processing."""

import numpy as np
import re
import cv2

def showVideo(filename):
	pass

def video2image(filename, n=0): 
	u"""Read mpeg video and divide into jpeg images.
	@param  filename:video filename
	@param  n       :number of export images (if n=0, this function exports all images in video.)  
	@return count   :number of exported images
	"""
	count = 1
	fnin = filename[:filename.rfind('.')] #拡張子をとったファイル名を取得

	cap = cv2.VideoCapture(filename)
	
	if n == 0:
		n = int(cap.get(7))  #CV_CAP_PROP_FRAME_COUNT
	fps = round(cap.get(5))  #CV_CAP_PROP_FPS
	height = int(cap.get(4)) #CV_CAP_PROP_FRAME_HEIGHT
	width = int(cap.get(3))  #CV_CAP_PROP_FRAME_WIDTH

	print('frame num =', n)
	print('fps       =', fps)
	print('hright    =', height)
	print('width     =', width, '\n')

	for i in np.arange(n):
		count = i+1
		fnout = '%06d' % count
		fnout = fnin + fnout + '.jpg'
		ret, frame = cap.read()
		cv2.imwrite(fnout, frame)

	print('Export', count, 'jpeg Images.')
	return count

def image2video():
	pass

#filename = 'test.mov'
#n = video2image(filename, )
#print(n)