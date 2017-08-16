# 
# embed_in_freq.py
# Created by pira on 2017/08/01.
#

#coding: utf-8

from VideoDigitalWatermarking import *

fnin  = 'test.bmp'
fnout = 'test_embeded.bmp'

secret_data = [1,1,1,1,0,0,0,0]

rgb_data = readColorImage(fnin)
ycc_data = rgb2ycc(rgb_data)
y_data   = get_y(ycc_data)
dct_data = dct_dim2(y_data)
embeded_dct_y_data = embedBitReplace(dct_data, secret_data, bit=5, interval=100)
embeded_y_data = idct_dim2(embeded_dct_y_data)

#replace y_data to embeded_y_data
height = ycc_data.shape[0]
width  = ycc_data.shape[1]
for i in np.arange(height):
	for j in np.arange(width):
		ycc_data[i][j][0] = embeded_y_data[i][j]

embeded_rgb_data = ycc2rgb(ycc_data)

#print(rgb_data[0][0], embeded_rgb_data[0][0])

writeImage(fnout, embeded_rgb_data)
