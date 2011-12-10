#!/usr/bin/env python

from mersenne import mersenne

def lucaslehmer(p):
	s = 4
	m = mersenne(p)
	#m = 2**p-1
	for i in xrange(p-2):
		s = ((s*s)-2)%m
	return s==0

if __name__ == "__main__":
	import sys
	print lucaslehmer(int(sys.argv[1]))
