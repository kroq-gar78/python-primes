#!/usr/python/env python

# Generate the nth Fermat number (index starting at 0)
# Created by Aditya Vaidya <kroq.gar78@gmail.com>

import math

def fermat_num(n):
	return (1<<(1<<n))+1

if __name__ == "__main__":
	import sys
	print fermat_num(int(sys.argv[1]))
