#!/usr/bin/env python

# Factorize a number into its prime factors, and find their exponents, too
# Created by Aditya Vaidya <kroq.gar78@gmail.com>

import math

def factorize(n,primes=[2]):
	factorization = {}
	factor = 0
	for i in primes:
		if(n%i==0):
			factor=i
			break
	if factor==0:
		for i in xrange(primes[len(primes)-1],int(math.sqrt(n))+1):
			ifprime = True
			for j in primes:
				if i%j==0:
					ifprime = False
					break
			if ifprime:
				if(n%i==0):
					factor=i
					break
				if(not i in primes): primes.append(i)
		if factor==0: return {n:1}
			
	exp=0
	while(n%factor==0):
		exp+=1
		n/=factor
	factorization[factor]=exp
	if(n!=factor and n!=1):
		results=factorize(n)
		for i in results.keys():
			factorization[i]=results[i]
	return factorization

# Uses pfactors.py to first find the prime factors, and then
# calculate the exponents
def factorize2(n):
	from pfactors import pfactors
	factorization = {}
	factors = pfactors(n)
	for i in factors:
		exp=0
		while(n%i==0):
			exp+=1
			n/=i
		factorization[i]=exp
	return factorization

if __name__ == "__main__":
	import sys
	print factorize(int(sys.argv[1]))
