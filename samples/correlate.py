#
# correlate.py
# Created by pira on 2017/08/15.
#

#coding: utf-8

from VideoDigitalWatermarking import *

#test
x=[1,-1,1]
y=[1,-1,1]

cycle = correlate(x, y, CYCLE)
noncylcle = correlate(x, y, NON_CYCLE)

print('CYCLE     =', cycle)
print('NON CYCLE =', noncylcle)