#
# embed_ccc.py
# Created by pira on 2017/08/14.
#

#coding: utf-8

from VideoDigitalWatermarking import *

secret_data = [1,1,1,1,0,0,0,0]
secret_length = len(secret_data)

print('CCC')
ccc = generateCCC(2)
print(ccc, '\n')

#Embed
basic = createBasicSeq(ccc, secret_length, tau=1)
print('basic = ', basic, '\n')

es = createEmbedSeq(basic, secret_data, a=1, tau=1)
print('Embed Sequence =', es, '\n')

#Extract
secret = extractCCC(ccc, es, secret_length, tau=1, ch=1)
print('secret =', secret)