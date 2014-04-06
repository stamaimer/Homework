#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

argc = 3

wbuffer = [None for _ in range(80)]

hbuffer = ["0110101000001001111001100110011111110011101111001100100100001000",
	   "1011101101100111101011101000010110000100110010101010011100111011",
	   "0011110001101110111100110111001011111110100101001111100000101011",
	   "1010010101001111111101010011101001011111000111010011011011110001",
	   "0101000100001110010100100111111110101101111001101000001011010001",
	   "1001101100000101011010001000110000101011001111100110110000011111",
	   "0001111110000011110110011010101111111011010000011011110101101011",
	   "0101101111100000110011010001100100010011011111100010000101111001"]

kbuffer = [0x428a2f98d728ae22, 0x7137449123ef65cd, 0xb5c0fbcfec4d3b2f, 0xe9b5dba58189dbbc, 
	   0x3956c25bf348b538, 0x59f111f1b605d019, 0x923f82a4af194f9b, 0xab1c5ed5da6d8118,
	   0xd807aa98a3030242, 0x12835b0145706fbe, 0x243185be4ee4b28c, 0x550c7dc3d5ffb4e2,
	   0x72be5d74f27b896f, 0x80deb1fe3b1696b1, 0x9bdc06a725c71235, 0xc19bf174cf692694,
	   0xe49b69c19ef14ad2, 0xefbe4786384f25e3, 0x0fc19dc68b8cd5b5, 0x240ca1cc77ac9c65,
	   0x2de92c6f592b0275, 0x4a7484aa6ea6e483, 0x5cb0a9dcbd41fbd4, 0x76f988da831153b5,
	   0x983e5152ee66dfab, 0xa831c66d2db43210, 0xb00327c898fb213f, 0xbf597fc7beef0ee4,
	   0xc6e00bf33da88fc2, 0xd5a79147930aa725, 0x06ca6351e003826f, 0x142929670a0e6e70,
	   0x27b70a8546d22ffc, 0x2e1b21385c26c926, 0x4d2c6dfc5ac42aed, 0x53380d139d95b3df,
	   0x650a73548baf63de, 0x766a0abb3c77b2a8, 0x81c2c92e47edaee6, 0x92722c851482353b,
	   0xa2bfe8a14cf10364, 0xa81a664bbc423001, 0xc24b8b70d0f89791, 0xc76c51a30654be30,
	   0xd192e819d6ef5218, 0xd69906245565a910, 0xf40e35855771202a, 0x106aa07032bbd1b8,
	   0x19a4c116b8d2d0c8, 0x1e376c085141ab53, 0x2748774cdf8eeb99, 0x34b0bcb5e19b48a8,
	   0x391c0cb3c5c95a63, 0x4ed8aa4ae3418acb, 0x5b9cca4f7763e373, 0x682e6ff3d6b2b8a3,
	   0x748f82ee5defb2fc, 0x78a5636f43172f60, 0x84c87814a1f0ab72, 0x8cc702081a6439ec,
	   0x90befffa23631e28, 0xa4506cebde82bde9, 0xbef9a3f7b2c67915, 0xc67178f2e372532b,
	   0xca273eceea26619c, 0xd186b8c721c0c207, 0xeada7dd6cde0eb1e, 0xf57d4f7fee6ed178,
	   0x06f067aa72176fba, 0x0a637dc5a2c898a6, 0x113f9804bef90dae, 0x1b710b35131c471b,
	   0x28db77f523047d84, 0x32caab7b40c72493, 0x3c9ebe0a15c9bebc, 0x431d67c49c100d4c,
	   0x4cc5d4becb3e42b6, 0x597f299cfc657e2a, 0x5fcb6fab3ad6faec, 0x6c44198c4a475817] 

def ror(str2ror, step):

	str2ror = list(str2ror)

	str2ror.reverse()

	partst = str2ror[:step]

	partst.reverse()

	partnd = str2ror[step:]

	partnd.reverse()

	return ''.join(partst + partnd)

def shr(str2shr, step):

	length = len(str2shr)

	str2shr = list(str2shr)

	for i in range(length - step):

		str2shr[i] = str2shr[i + step]

	for i in range(step):

		str2shr[length - i - 1] = '0'

	return ''.join(str2shr)

def sigma0(var):

	tmp = bin(int(ror(var,  1), 2) + int(ror(var,  8), 2) + int(shr(var,  7), 2))[2:].zfill(64)

	return tmp[len(tmp)-64:len(tmp)]

def sigma1(var):
	
	tmp = bin(int(ror(var, 19), 2) + int(ror(var, 61), 2) + int(shr(var,  6), 2))[2:].zfill(64)

	return tmp[len(tmp)-64:len(tmp)]

def sigma2(var):
	
	tmp = bin(int(ror(var, 14), 2) ^ int(ror(var, 18), 2) ^ int(ror(var, 41), 2))[2:].zfill(64)

	return tmp[len(tmp)-64:len(tmp)]

def sigma3(var):
	
	tmp = bin(int(ror(var, 28), 2) ^ int(ror(var, 34), 2) ^ int(ror(var, 39), 2))[2:].zfill(64)

	return tmp[len(tmp)-64:len(tmp)]

def chr():
	
	tmp = bin((int(hbuffer[4], 2) and int(hbuffer[5], 2)) ^ (not int(hbuffer[4], 2) and int(hbuffer[6], 2)))[2:].zfill(64)

	return tmp[len(tmp)-64:len(tmp)]

def maj():
	
	tmp = bin((int(hbuffer[0], 2) and int(hbuffer[1], 2)) ^ (int(hbuffer[0], 2) and int(hbuffer[2], 2)) ^ (int(hbuffer[1], 2) and int(hbuffer[2], 2)))[2:].zfill(64)

	return tmp[len(tmp)-64:len(tmp)]

def gen(str2gen):

	for i in range(16):

		wbuffer[i] = str2gen[64*i:64*(i+1)]

	for i in range(16, 80):

		tmp = bin(
				  int(sigma1(wbuffer[i -  2]), 2)
				+ int(wbuffer[i -  7], 2)	
				+ int(sigma0(wbuffer[i - 15]), 2) 
				+ int(wbuffer[i - 16], 2)

			 )[2:].zfill(64)

		wbuffer[i] = tmp[len(tmp)-64:len(tmp)]

def process(str2pro):
	
	gen(str2pro)

	for i in range(80):

		t0 = int(hbuffer[7], 2) + int(wbuffer[i], 16) + int(chr(), 2) + int(sigma2(hbuffer[4]), 2)

		t1 = int(maj(), 2) + int(sigma3(hbuffer[0]), 2)

		hbuffer[7] = hbuffer[6]
		hbuffer[6] = hbuffer[5]
		hbuffer[5] = hbuffer[4]

		tmp = bin(int(hbuffer[3], 2) + t0)[2:].zfill(64)

		hbuffer[4] = tmp[len(tmp)-64:len(tmp)]

		hbuffer[3] = hbuffer[2]
		hbuffer[2] = hbuffer[1]
		hbuffer[1] = hbuffer[0]

		tmp = bin(t0 + t1)[2:].zfill(64)

		hbuffer[0] = tmp[len(tmp)-64:len(tmp)]

def str2bin(str2convert):

	return ''.join([bin(ord(char))[2:].zfill(8) for char in str2convert])

def pad(str2pad):

	length = len(str2pad)

	size = 896 - length % 1024

	if not size:

		size = 1920 - length % 1024

	return ''.join([str2pad, '1', ''.join(['0' for _ in range(size - 1)]), bin(length)[2:].zfill(128)])

def sha512(str2hash):

	str2hash = str2bin(str2hash)

	str2hash = pad(str2hash)

	if len(str2hash) % 1024 == 0:

		length = len(str2hash) / 1024

		print "there are", length, "pkgs to process"

		for i in range(length):
		
			process(str2hash[1024*i:1024*(i+1)]) 

	print ''.join([hex(int(hbuffer[i], 2))[2:-1] for i in range(8)])

if argc != len(sys.argv):

	print("write usage in here...")

	exit(1)

if '-s' == sys.argv[1]:

	sha512(sys.argv[2])

	exit(0)

if '-f' == sys.argv[1]:

	file = open(sys.argv[2], 'r')

	sha512(file.read(-1))

	file.close()

	exit(0)	