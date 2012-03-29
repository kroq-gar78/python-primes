#!/usr/bin/env python

# Calculates Mesenne numbers, which are
# 2^p-1

def mersenne(p):
	return (1<<p)-1
	
if __name__ == "__main__":
	import sys
	print mersenne(int(sys.argv[1]))
