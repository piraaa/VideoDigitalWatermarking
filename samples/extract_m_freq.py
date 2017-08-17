#
# extract_m_freq.py
# Created by pira on 2017/08/16.
#

#coding: utf-8

from VideoDigitalWatermarking import *
import math


fn_cover  = 'test.bmp'
fn_stego  = 'test_embeded.bmp'

secret_length = 7 #secret infomation length

N = math.ceil(math.log2(secret_length+1))
m = generateM(N)

print('m =', m, '\n')

rgb_cover = readColorImage(fn_cover)
rgb_stego = readColorImage(fn_stego)

ycc_cover = rgb2ycc(rgb_cover)
ycc_stego = rgb2ycc(rgb_stego)
y_cover   = get_y(ycc_cover)
y_stego   = get_y(ycc_stego)
dct_cover = dct_dim2(y_cover)
dct_stego = dct_dim2(y_stego)

secret_data = extractMseq(dct_cover, dct_stego, secret_length, m, tau=1)
print(secret_data)
