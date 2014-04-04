#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

argc = 3

def init():
	hbuffer = [
			   0x6a09e667f3bcc908, 0xbb67ae8584caa73b, 
			   0x3c6ef372fe94f82b, 0xa54ff53a5f1d36f1, 
			   0x510e527fade682d1, 0x9b05688c2b3e6c1f, 
			   0x1f83d9abfb41bd6b, 0x5be0cd19137e2179,
			  ]

	kbuffer = [
			   0x428a2f98d728ae22, 0x7137449123ef65cd,
        	   0xb5c0fbcfec4d3b2f, 0xe9b5dba58189dbbc,
        	   0x3956c25bf348b538, 0x59f111f1b605d019,
        	   0x923f82a4af194f9b, 0xab1c5ed5da6d8118,
        	   0xd807aa98a3030242, 0x12835b0145706fbe,
        	   0x243185be4ee4b28c, 0x550c7dc3d5ffb4e2,
        	   0x72be5d74f27b896f, 0x80deb1fe3b1696b1,
        	   0x9bdc06a725c71235, 0xc19bf174cf692694,
        	   0xe49b69c19ef14ad2, 0xefbe4786384f25e3,
        	   0x0fc19dc68b8cd5b5, 0x240ca1cc77ac9c65,
        	   0x2de92c6f592b0275, 0x4a7484aa6ea6e483,
        	   0x5cb0a9dcbd41fbd4, 0x76f988da831153b5,
        	   0x983e5152ee66dfab, 0xa831c66d2db43210,
        	   0xb00327c898fb213f, 0xbf597fc7beef0ee4,
        	   0xc6e00bf33da88fc2, 0xd5a79147930aa725,
        	   0x06ca6351e003826f, 0x142929670a0e6e70,
        	   0x27b70a8546d22ffc, 0x2e1b21385c26c926,
        	   0x4d2c6dfc5ac42aed, 0x53380d139d95b3df,
        	   0x650a73548baf63de, 0x766a0abb3c77b2a8,
        	   0x81c2c92e47edaee6, 0x92722c851482353b,
        	   0xa2bfe8a14cf10364, 0xa81a664bbc423001,
        	   0xc24b8b70d0f89791, 0xc76c51a30654be30,
        	   0xd192e819d6ef5218, 0xd69906245565a910,
        	   0xf40e35855771202a, 0x106aa07032bbd1b8,
        	   0x19a4c116b8d2d0c8, 0x1e376c085141ab53,
        	   0x2748774cdf8eeb99, 0x34b0bcb5e19b48a8,
        	   0x391c0cb3c5c95a63, 0x4ed8aa4ae3418acb,
        	   0x5b9cca4f7763e373, 0x682e6ff3d6b2b8a3,
        	   0x748f82ee5defb2fc, 0x78a5636f43172f60,
        	   0x84c87814a1f0ab72, 0x8cc702081a6439ec,
        	   0x90befffa23631e28, 0xa4506cebde82bde9,
        	   0xbef9a3f7b2c67915, 0xc67178f2e372532b,
        	   0xca273eceea26619c, 0xd186b8c721c0c207,
        	   0xeada7dd6cde0eb1e, 0xf57d4f7fee6ed178,
        	   0x06f067aa72176fba, 0x0a637dc5a2c898a6,
        	   0x113f9804bef90dae, 0x1b710b35131c471b,
        	   0x28db77f523047d84, 0x32caab7b40c72493,
        	   0x3c9ebe0a15c9bebc, 0x431d67c49c100d4c,
        	   0x4cc5d4becb3e42b6, 0x597f299cfc657e2a,
        	   0x5fcb6fab3ad6faec, 0x6c44198c4a475817, 
        	  ] 

def gcd(a, b):

	if a == 0 or b == 0:

		return a + b

	while b < 0:

		c = a % b

		a = b

		b = c

	return a

def ror(str2ror, step):

	step = step % len(str2ror)

	if step == 0:

		return str2ror

	for i in range(gcd(len(str2ror), step)):

		index = i

		tmp = str2ror[index]

		while 1:

			index = (index + step) % len(str2ror)

			tmptmp = str2ror[index]

			str2ror[index] = tmp

			tmp = tmptmp

			if index == i:

				break

	return str2ror

def shr(str2shr, step):

	return bin(int(str2shr, 2) << step)[2:].zfill(64)

def sigma0(var):

	return bin(int(ror(var, 1), 2) + int(ror(var, 8), 2) + int(shr(var, 7), 2))[2:].zfill(64)

def sigma1(var):
	
	return bin(int(ror(var, 19), 2) + int(ror(var, 61), 2) + int(shr(var, 6), 2))[2:].zfill(64)

def gen(str2gen):

	wbuffer = [None for _ in range(80)]

	for i in range(16):

		wbuffer[i] = str2gen[64*i:64*(i+1):1]

	for i in range(64):

		wbuffer[i + 16] = bin(int(sigma1(wbuffer[i + 14]), 2) + int(wbuffer[i + 9], 2) + int(sigma0(wbuffer[i + 1]), 2) + int(wbuffer[i], 2))[2:].zfill(64)

	return wbuffer

def update():
	pass

def str2bin(str2convert):

	return ''.join([bin(ord(char))[2:].zfill(8) for char in str2convert])

def pad(str2pad):

	srcstr = str2pad

	size = 896 - len(str2pad) % 1024

	if not size:

		size = 1920 - len(str2pad) % 1024

	return ''.join([str2pad, '1', ''.join(['0' for _ in range(size - 1)]), bin(len(srcstr))[2:].zfill(128)])

def sha512(str2hash):

	str2hash = str2bin(str2hash)

	print 'str2bin\n', str2hash

	str2hash = pad(str2hash) 

	print 'pad\n', str2hash

	print len(str2hash) % 1024

	for i in range(len(str2hash) / 1024):

		print gen(str2hash[1024*i:1024*(i+1):1])

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

			
	