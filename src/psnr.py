#
# psnr.py
# Created by pira on 2017/08/05.
#

#coding: utf-8
u"""For calculate PSNR(Peak Signal to Noise Ratio)."""

import math
import sys
import numpy as np

from image import getRgbLayer 

def calcPSNR(cover, stego):
	u"""Calculate PSNR.
	@param  cover : cover image
	@param  stego : stego image 
	@return psnr  : PSNR [dB]
	"""

	print('cover shape =', cover.shape)
	print('stego shape =', stego.shape)

	#if cover and stego are RGB color images:
	if cover.shape[2] == stego.shape[2] == 3:
		layer_num = 3 
	#elif cover and stego are gray images:
	elif cover.shape[2] == stego.shape[2] == 1:
		layer_num = 1
	else:
		print('Please give an appropriate images.')
		print('You can use only 3 dimensoin RGB image or 2 dimension gray image.')
		sys.exit()

	p = 255 #maximum value of RGB
	mse = 0

	for i in np.arange(layer_num):
		mse += _calcMSE(getRgbLayer(cover,i), getRgbLayer(stego,i))

	mse = mse/layer_num

	psnr = 10 * (math.log10(p) - math.log10(mse))

	return psnr

def _calcMSE(cover, stego):
	if cover.shape[0] == stego.shape[0] and cover.shape[1] == stego.shape[1]:
		height = cover.shape[0]
		width  = cover.shape[1]
	else:
		print('Please give an appropriate images.')
		print('Cover image and stego image are not the same size.')
		sys.exit()

	mse = 0
	for i in np.arange(height):
		for j in np.arange(width):
			mse += (cover[i][j] - stego[i][j])**2
	mse = (1/(height*width)) * mse 
	return mse

#test
#a = np.array([[[11,10,10],[20,20,20],[30,30,30]],[[10,10,10],[20,20,20],[30,30,30]],[[10,10,10],[20,20,20],[30,30,30]]])
#b = np.array([[[10,10,10],[20,20,20],[30,30,30]],[[10,10,10],[20,20,20],[30,30,30]],[[10,10,10],[20,20,20],[30,30,30]]])
#psnr = calcPSNR(a, b)
#print('psnr =', psnr)
