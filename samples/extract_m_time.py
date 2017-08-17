#
# extract_m_time.py
# Created by pira on 2017/08/15.
#

#coding: utf-8

from VideoDigitalWatermarking import *
import math

fn_cover  = 'test.bmp'
fn_stego = 'test_embeded.bmp'

secret_length = 7 #secret infomation length
N = math.ceil(math.log2(secret_length+1))
m = generateM(N)

print('m =', m, '\n')

rgb_cover = readColorImage(fn_cover)
rgb_stego = readColorImage(fn_stego)

red_cover   = getRgbLayer(rgb_cover, rgb=RED)
red_stego   = getRgbLayer(rgb_stego, rgb=RED)

secret_data = extractMseq(red_cover, red_stego, secret_length, m, tau=1)
print(secret_data)
