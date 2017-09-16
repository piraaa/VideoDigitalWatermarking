#
# ccc.py
# Created by pira on 2017/07/28.
#

#coding: utf-8
u"""For Complete Complementary Code."""

import numpy as np
from numpy import random
from numpy import diag
import sys

#CCC(N,N,N**2)を生成
def generateCCC(N):
	u"""Create CCC.
 	@param  N   : CCC size
 	@return CCC : CCC(N,N,N**2)
	"""
	
	#対角成分
	random.seed(N)
	r = np.array(random.choice([1,-1],N))
	if sum(r) == N or sum(r) == -N:
		sys.stderr.write('ERROR: invalid seed number.')
		sys.exit(-1)

	#アダマール行列を生成
	H = np.array([[(-1)**bin(i&j).count('1') for i in np.arange(N)] for j in np.arange(N)])

	#CCCを生成
	CCC = np.empty((N,N,N*N))
	A = np.dot(H,diag(r))
	B = np.dot(diag(r),H)
	for i in np.arange(N):
		for j in np.arange(N):
			for k in np.arange(N):
				a = A[i,k]
				for l in np.arange(N):
					CCC[i,j,N*k+l] = a*H[k,l]*B[j,l]
	return CCC

#test
#ccc = generateCCC(2)
#print(ccc)