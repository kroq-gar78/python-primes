#!/usr/bin/env python

# Calculate the number of positive integer divisors of 'n'
# Created by Aditya Vaidya <kroq.gar78@gmail.com>

from factorize import factorize

def tau(n):
	pfactors = factorize(n)
	product = 1
	for i in pfactors.keys():
		product *= pfactors[i]+1
	return product

if __name__ == "__main__":
	import sys
	print tau(int(sys.argv[1])) 
