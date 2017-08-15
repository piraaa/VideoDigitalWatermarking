#
# divide_image_into_blocks.py
# Created by pira on 2017/08/15.
#

#coding: utf-8

from VideoDigitalWatermarking import *

filename = 'test.bmp'
image = readColorImage(filename)

blocks = colorimage2block(image, [128,128])
#print(blocks.shape)

for i in np.arange(blocks.shape[0]):
	for j in np.arange(blocks.shape[1]):
		writeImage(str(i*blocks.shape[1]+j+1) + '.bmp', blocks[i][j])