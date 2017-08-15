#
# msequence.py
# Created by pira on 2017/07/28.
#

#coding: utf-8
u"""For M-Sequence."""

import numpy as np

def generateM(N):
	u"""Create M-Sequence.
 	@param  N : length 2**N-1
 	@return m : M-Sequence
	"""

	p = pow(2, N)
	m = [0] * (p-1)

	for i in np.arange(1,p,2): 
		f = p^i
		a = p
		#i = int()
		for j in np.arange(N, p):
			if (a&p) == p:
				a ^= f
			if a == 1:
				break
			a <<= 1
		if j == p-1:
			init = 1
			lfsr = init & (p-1)
			f >>= 1
			for k in np.arange(0, p-1):
				lfsr = (lfsr>>1)^(-(int)(lfsr&1) & f)
				m[k] = (lfsr&1) * 2-1
			return m

#test
#m = generateM(3)
#print(m)