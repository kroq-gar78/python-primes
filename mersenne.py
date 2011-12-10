#!/usr/bin/env python

import sys

def mersenne(p):
	n = 1
	for i in xrange(p):
		n <<= 1
	return n
	
if __name__ == "__main__":
	print mersenne(int(sys.argv[1]))
