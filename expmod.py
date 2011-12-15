#!/usr/bin/python

# Fast algorithm for modular exponentiation


def expmod(a,b,c):
	x = 1
	while(b>0):
		if(b&1==1): x = (x*a)%c
		a=(a*a)%c
		b >>= 1
	return x%c

if __name__ == "__main__":
	import sys
	print expmod(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))
