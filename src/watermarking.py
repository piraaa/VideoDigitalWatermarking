#
# watermarking.py
# Created by pira on 2017/07/26.
#

#coding: utf-8
u"""Image Watermarking"""

#using for add_lsb mode.
TIME_DOMAIN = 1
DCT_DOMAIN  = 0

def add_lsb(cover, secret, mode=0):
	u"""Embed 1 bit secret information by changing LSB.
 	@param  cover :cover data
 	@param  secret:secret data (1 bit)
 	@param  mode  :mode 0 is used for dct-domain, mode 1 is used for time-domain.(mode 1 avoids overflow that pxcel value is more than 255.)
 	@return stego :srego data
	"""

	if secret == 0:
		if cover%2 == 0:
			stego = cover
		else:
			stego = cover + 1
			if mode == 1:
				if stego > 255:
					stego -= 2
	elif secret == 1:
		if cover%2 == 0:
			stego = cover + 1
		else:
			stego = cover
	return stego

def check_lsb(data):
	u"""Extract 1 bit secret information by chacking LSB.
 	@param  data   :stego data
 	@return secret :1 bit secret information
	"""
	if data%2 == 0:
		return 0
	elif data%2 == 1:
		return 1

def 