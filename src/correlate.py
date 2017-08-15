#
# correlate.py
# Created by pira on 2017/08/15.
#

#coding: utf-8


u"""Calculate correlate functions."""

import numpy as np
import sys

NON_CYCLE = 0
CYCLE = 1

def correlate(data1, data2, cycle=NON_CYCLE):
	u"""Calculate correlate function.
	@param  data1 : 
	@param  data2 : 
	@param  cycle : CYCLE or NON_SYCLE. Default is NON_CYCLE.
	@return correlate : correlate list
	"""
	if cycle == NON_CYCLE:
		correlate = np.correlate(data1, data2, 'full')

	elif cycle == CYCLE:
		N = len(data1)
		correlate = list()

		for i in np.arange(-N+1, N):
			ans = 0
			shift_data1 = np.roll(data1,i)
			for j in range(0,N):
				ans += shift_data1[j]*data2[j]
			correlate.append(ans)

		correlate = np.array(correlate)

	else:
		print('Invalid argument.')
		print('Please review parameter in correlate function.')
		sys.exit()

	return correlate

#test
#x=[1,-1,1]
#y=[1,-1,1]
#cycle = correlate(x, y, CYCLE)
#noncylcle = correlate(x, y, NON_CYCLE)
#print('CYCLE     =', cycle)
#print('NON CYCLE =', noncylcle)