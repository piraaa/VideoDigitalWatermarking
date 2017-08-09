#
# sample2.py
# Created by pira on 2017/08/04.
#

#coding: utf-8

from VideoDigitalWatermarking import *
import numpy as np

fn_cover = 'test1.png'
fn_stego = 'test2.png'

rgb_cover = readColorImage(fn_cover)
rgb_stego = readColorImage(fn_stego)

#print(rgb_cover[0][0], rgb_stego[0][0])

ycc_cover = rgb2ycc(rgb_cover)
ycc_stego = rgb2ycc(rgb_stego)
y_cover   = get_y(ycc_cover)
y_stego   = get_y(ycc_stego)
dct_cover = dct_dim2(y_cover)
dct_stego = dct_dim2(y_stego)

#print(dct_cover[0][0], dct_stego[0][0])

secret_data = extractBitReplace(dct_cover, dct_stego, 8, bit=2, interval=100)
print(secret_data)