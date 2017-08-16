#
# extract_from_time.py
# Created by pira on 2017/08/09.
#

#coding: utf-8

from VideoDigitalWatermarking import *

fn_cover  = 'test.bmp'
fn_stego = 'test_embeded.bmp'

rgb_cover = readColorImage(fn_cover)
rgb_stego = readColorImage(fn_stego)

red_cover   = getRgbLayer(rgb_cover, rgb=RED)
red_stego   = getRgbLayer(rgb_stego, rgb=RED)

secret_data = extractBitReplace(red_cover, red_stego, 8, bit=1, interval=0)
print(secret_data)