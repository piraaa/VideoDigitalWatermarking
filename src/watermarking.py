#
# watermarking.py
# Created by pira on 2017/07/26.
#

#coding: utf-8
u"""For image watermarking."""

import sys
import numpy as np

TIME_DOMAIN = 1
DCT_DOMAIN  = 0

def embed_lsb(cover, secret, interval=0):
	u"""Embed secret informations by changing LSB.
 	@param  cover   :cover data (2 dimension np.ndarray)
 	@param  secret  :0 or 1 secret information (list)
 	@param  interval:ebmed interval
 	@return stego   :srego data (2 dimension np.ndarray)
	"""
	height = cover.shape[0]
	width  = cover.shape[1]
	es_length = len(secret) * (1+interval) #Embeded Sequense length

	if height*width < es_length:
		print('Secret information is over the limit of embeded.')
		print('Please review the cover image, secret information or interval.')
		sys.exit()

	#create embeded sequense
	es = np.zeros(es_length)
	for i, secret_bit in enumerate(secret):
			es[i*(interval+1)] = secret_bit

	cover = _image2vrctor(cover)
	stego = cover

	for i, secret_bit in enumerate(es):
		stego[i] = _add_lsb(cover[i], secret_bit)

	stego = _vector2image(stego, height, width)

	return stego

#def extract_lsb():

def _add_lsb(cover, secret, mode=0):
	u"""Embed 1 bit secret information by changing LSB.
 	@param  cover :cover data
 	@param  secret:secret data (1 bit)
 	@param  mode  :mode 0 is used for dct-domain, mode 1 is used for time-domain.(mode 1 avoids overflow that pxcel value is more than 255.)
 	@return stego :srego data
	"""
	stego = 0
	cover = round(cover)
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

def _check_lsb(data):
	u"""Extract 1 bit secret information by chacking LSB.
 	@param  data   :stego data
 	@return secret :1 bit secret information
	"""

	if data%2 == 0:
		return 0
	elif data%2 == 1:
		return 1

def _image2vrctor(img):
	u"""Convert image to vector.
 	@param  img   :2 dimension image data
 	@return vector:1 dimension image data
	"""
	height = img.shape[0]
	width  = img.shape[1]
	len = height * width
	vector = np.empty(len)
	for i in np.arange(height):
		for j in np.arange(width):
			vector[i*height+j] = img[i][j]
	return vector

def _vector2image(vector, height, width):
	u"""Convert vector to image.
 	@param  vector:1 dimension image data
 	@return image :2 dimension image data
	"""
	image = np.empty([height, width])
	for i in np.arange(height):
		for j in np.arange(width):
			image[i][j] = vector[i*height+j]
	return image
