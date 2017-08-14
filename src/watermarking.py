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

def embedBitReplace(cover, secret, bit=1, interval=0):
	u"""Embed secret informations by changing bit.
	@param  cover   :cover data (2 dimension np.ndarray)
	@param  secret  :0 or 1 secret information list
	@param  bit     :number of replaced bit (It's recommended to be close to the LSB.)
	@param  interval:ebmed interval
	@return stego   :srego data (2 dimension np.ndarray)
	"""
	height = cover.shape[0]
	width  = cover.shape[1]
	es_length = len(secret) * (1+interval) #Embeded Sequence length

	if height*width < es_length:
		print('Secret information is over the limit of embeded.')
		print('Please review the cover image, secret information or interval.')
		sys.exit()

	#create embeded sequence
	es = np.zeros(es_length)
	for i, secret_bit in enumerate(secret):
			es[i*(interval+1)] = secret_bit

	cover = _image2vrctor(cover)
	stego = cover

	for i, secret_bit in enumerate(es):
		stego[i] = _addBitReplace(cover[i], secret_bit, bit)

	stego = _vector2image(stego, height, width)

	return stego

def extractBitReplace(cover, stego, secret_length, bit=1, interval=0):
	u"""Extract secret informations by chacking LSB.
	@param  cover        :cover data (2 dimension np.ndarray)
	@param  stego        :stego data (2 dimension np.ndarray)
	@param  secret_length:length of secret information
	@param  bit          :number of replaced bit 
	@param  interval     :embed interval
	@return secret       :extracted secret information
	"""
	secret_data = np.zeros(secret_length)

	cover = _image2vrctor(cover)
	stego = _image2vrctor(stego)
	#data  = stego - cover

	for i in np.arange(secret_length):
		#print(stego[i*(interval+1)])
		secret_data[i] = _checkBitReplace(stego[i*(interval+1)], bit)

	return secret_data

def _addBitReplace(cover, secret, bit=1):
	u"""Embed 1 bit secret information by changing LSB.
	@param  cover  :1 pixel cover data
	@param  secret :i bit secret information
	@param  bit    :number of replaced bit
	@return stego  :1 pixel srego data
	"""
	stego = int(round(cover))
	stego = format(stego, '08b')
	stego = stego[::-1]

	if secret == 0:
		if stego[bit-1] == '0':
			pass
		elif stego[bit-1] == '1':
			stego = stego[:(bit-1)] + '0' + stego[bit:]
	elif secret == 1:
		if stego[bit-1] == '0':
			stego = stego[:(bit-1)] + '1' + stego[bit:]
		elif stego[bit-1] == '1':
			pass

	stego = stego[::-1]
	stego = int(stego, 2)
	return stego

def _checkBitReplace(data, bit=1):
	u"""Extract 1 bit secret information by chacking LSB.
	@param  data   :stego data
	@param  bit    :number of replaced bit
	@return secret :1 bit secret information
	"""
	data = int(round(data))
	data = format(data, '08b')
	data = data[::-1]

	if data[bit-1] == '0':
		return 0
	elif data[bit-1] == '1':
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

def zero2minus(zero_data):
	u"""Convert 0 to -1.
	@param  zero_data :secret information represented by 0 and 1.
	@return minus_data:secret information represented by -1 and 1.
	"""
	minus_data = zero_data
	for i,data in enumerate(zero_data):
		if data == 0:
			minus_data[i] = -1
	return minus_data

def minus2zero(minus_data):
	u"""Convert -1 to 0.
	@param  minus_data:secret information represented by -1 and 1.
	@return zero_data :secret information represented by 0 and 1.
	"""
	zero_data = minus_data
	for i,data in enumerate(minus_data):
		if data == -1:
			zero_data[i] = 0
	return zero_data

