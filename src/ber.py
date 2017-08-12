#
# ber.py
# Created by pira on 2017/08/05.
#

#coding: utf-8
u"""Calculate BER(Bit Error Rate)."""

import sys

def calcBER(data1, data2):
	u"""Calculate Bit Error Rate.
	@param  data1 : result data
	@param  data2 : answer data
	@return ber   : bit error rate [%]
	"""
	if len(data1) != len(data2):
		print('The input data have different length.')
		print('Please give data with the same length.')
		sys.exit()

	error_bits = 0
	for (d1,d2) in zip(data1,data2):
		if d1 != d2:
			error_bits += 1

	data_len = len(data1)
	ber = (error_bits / data_len) * 100

	return ber

#test
#data1 = [1,0,1,0,1,0,1,0]
#data2 = [1,1,1,1,0,0,0,0]
#ber = calcBER(data1, data2)
#print('BER =', ber, '[%]')
