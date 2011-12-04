#!/usr/bin/python

import sys

def expmod(a,b,c):
	x,y = 1,a
	while(b>0):
		if(b&1==1): x = (x*y)%c
		y=(y*y)%c
		b >>= 1
	return x%c

if __name__ == "__main__":
	print expmod(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))
