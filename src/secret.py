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

def str2bi(secret_str):
	u"""Convert string to binary.
	@param  secret_str : string secret information
	@return secret_bi : binary secret information 
	"""
	pass


def bi2str(secret_bi):
	u"""Convert binary to string.
	@param  secret_bi : binary secret information
	@return secret_str : string secret information 
	"""
	pass
