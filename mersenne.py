#!/usr/bin/env python

import sys

# Calculates Mesenne numbers, which are
# 2^p-1

def mersenne(p):
	return (1<<p)-1
	
if __name__ == "__main__":
	print mersenne(int(sys.argv[1]))
