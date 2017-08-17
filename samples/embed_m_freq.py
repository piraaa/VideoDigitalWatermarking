#
# embed_m_freq.py
# Created by pira on 2017/08/16.
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
ycc_data = rgb2ycc(rgb_data)
y_data   = get_y(ycc_data)
dct_data = dct_dim2(y_data)
embeded_dct_y_data = embedMseq(dct_data, secret_data, m, a=100, tau=1)
embeded_y_data = idct_dim2(embeded_dct_y_data)

#replace y_data to embeded_y_data
height = ycc_data.shape[0]
width  = ycc_data.shape[1]
for i in np.arange(height):
	for j in np.arange(width):
		ycc_data[i][j][0] = embeded_y_data[i][j]

embeded_rgb_data = ycc2rgb(ycc_data)

writeImage(fnout, embeded_rgb_data)
