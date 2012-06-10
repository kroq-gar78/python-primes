#!/usr/bin/env python

# Calculate the sum of all positive integer divisors of 'n'
# Created by Aditya Vaidya <kroq.gar78@gmail.com>

from factorize import factorize

def sigma(n):
	pfactors = factorize(n)
	product = 1
	for i in pfactors.keys():
		product *= ((i**(pfactors[i]+1)-1)/(i-1))
	return product

if __name__ == "__main__":
	import sys
	print sigma(int(sys.argv[1])) 
