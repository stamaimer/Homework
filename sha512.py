#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

argc = 3

def init():
	buffer = [
				'0x6a09e667f3bcc908',
				'0xbb67ae8584caa73b',
				'0x3c6ef372fe94f82b',
				'0xa54ff53a5f1d36f1',
				'0x510e527fade682d1',
				'0x9b05688c2b3e6c1f',
				'0x1f83d9abfb41bd6b',
				'0x5be0cd19137e2179',
			 ]

def update():
	pass

def str2bin(str2convert):

	return ''.join([bin(ord(char))[2:].zfill(8) for char in str2convert])

def pad(str2hash):

	size = 896 - len(str2hash) % 1024

	if not size:

		size = 1920 - len(str2hash) % 1024

	return ''.join([str2hash, '1', ''.join(['0' for i in range(size - 1)])])


def sha512(str2hash):

	str2hash = str2bin(str2hash)

	print 'str2bin\n', str2hash

	str2hash = pad(str2hash) 

	print 'pad\n', str2hash

if argc != len(sys.argv):

	print("write usage in here...")

if '-s' == sys.argv[1]:

	sha512(sys.argv[2])

if '-f' == sys.argv[1]:

	file = open(sys.argv[2], 'r')

	sha512(file.read(-1))

	file.close()

			
	