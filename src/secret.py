#
# secret.py
# Created by pira on 2017/08/09.
#

#coding: utf-8
u"""For Secret informations."""

import random
import numpy as np

def generateSecret(n):
	u"""Generate 0 or 1 random secret information for simulation.
	@param  n : length
	@return secret : secret information list
	"""
	secret = np.random.randint(2, size =n)
	return secret
