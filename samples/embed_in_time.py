# 
# embed_in_time.py
# Created by pira on 2017/08/09.
#

#coding: utf-8

from VideoDigitalWatermarking import *
import numpy as np

fnin  = 'test.bmp'
fnout = 'test_embeded.bmp'

secret_data = [1,1,1,1,0,0,0,0]

rgb_data = readColorImage(fnin)
red_data = getRgbLayer(rgb_data, rgb=RED)
embeded_red_data = embedBitReplace(red_data, secret_data, bit=1, interval=0)

#replace red_data to embeded_red_data
height = red_data.shape[0]
width  = red_data.shape[1]
for i in np.arange(height):
	for j in np.arange(width):
		rgb_data[i][j][RED] = embeded_red_data[i][j]

writeImage(fnout, rgb_data)
