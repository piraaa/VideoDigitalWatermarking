#
# BER.py
# Created by pira on 2017/08/15.
#

#coding: utf-8

from VideoDigitalWatermarking import *

data1 = [1,0,1,0,1,0,1,0]
data2 = [1,1,1,1,0,0,0,0]
ber = calcBER(data1, data2)
print('BER =', ber, '[%]')