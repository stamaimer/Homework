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

def pad(str):

	size = 896 - len(str) % 1024

	if not size:

		size = 1920 - len(str) % 1024



def sha512(str):
	print str2bin(str)

if argc != len(sys.argv):

	print("write usage in here...")

if '-s' == sys.argv[1]:

	sha512(sys.argv[2])

if '-f' == sys.argv[1]:

	file = open(sys.argv[2], 'r')

	sha512(file.read(-1))

	file.close()

			
	