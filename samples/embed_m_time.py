#
# embed_m_time.py
# Created by pira on 2017/08/15.
#

#coding: utf-8

from VideoDigitalWatermarking import *
import numpy as np
import math

fnin  = 'test.bmp'
fnout = 'test_embeded.bmp'

secret_data = [1,1,1,1,0,0,0]

secret_length = len(secret_data)
N = math.ceil(math.log2(secret_length+1))
m = generateM(N)

print('m =', m, '\n')

rgb_data = readColorImage(fnin)
red_data = getRgbLayer(rgb_data, rgb=RED)
embeded_red_data = embedMseq(red_data, secret_data, m, a=1, tau=1)

#replace red_data to embeded red_data
height = red_data.shape[0]
width  = red_data.shape[1]
for i in np.arange(height):
	for j in np.arange(width):
		rgb_data[i][j][RED] = embeded_red_data[i][j]

writeImage(fnout, rgb_data)
