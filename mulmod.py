#!/usr/bin/python

# Multiplicative Modulus
# calculates (a*b)%c, taking into account that a*b might overflow

import sys

def mulmod(a,b,c):
	x=0
	y=a%c
	while(b>0):
		if(b&1==1): x = (x+y)%c
		y = (y<<1)%c
		b >>= 1
	return x%c

if __name__ == "__main__":
	print mulmod(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))
