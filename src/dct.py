#
# dct.py
# Created by pira on 2017/07/31.
#

#coding: utf-8
u"""Discrete Cosine Transform"""

import numpy as np
import math

def dct_dim1(data):
	u"""1 dimension DCT.
 	@param  data:1 dimension data
 	@return data:1 dimension data conversion by DCT
	"""
	N = len(data)
	data = data.reshape(N,1)
	dct_matrix = _get_dctMatrix(N)
	dct_data = dct_matrix.dot(data)
	dct_data = dct_data.reshape(N)
	return dct_data

def dct_dim2(data):
	u"""2 dimension DCT.
 	@param  data:2 dimension data
 	@return data:2 dimension data conversion by DCT
	"""
	height = data.shape[0]
	width = data.shape[1]
	dct_data = np.empty((height,width))
	dct_matrix = _get_dctMatrix(height)
	dct_data = dct_matrix.dot(data)
	dct_matrix = _get_dctMatrix(width).T
	dct_data = dct_data.dot(dct_matrix)	
	return dct_data

def _get_dctMatrix(N):
	dct_matrix = np.empty((N,N))
	for k in np.arange(N):
		for n in np.arange(N):
			if k==0:
				dct_matrix[k][n] = 1/np.sqrt(N)
			else:
				dct_matrix[k][n] = math.sqrt(2/N)*np.cos((2*n+1)*k*np.pi/(2*N))
	return dct_matrix

#test
#data = np.array([1,2,3,4])
#data = np.array([[1,1,1,1],[2,1,2,1],[3,1,3,1],[4,1,4,1]])
#dct_data = dct_dim2(data)
#print(dct_data)