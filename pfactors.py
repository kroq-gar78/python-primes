#!/usr/bin/env python

# Find the prime factors of 'n'. Look at 'factorize.py' for finding
# their exponents, too.
# Created by Aditya Vaidya <kroq.gar78@gmail.com>

import math
from trialdiv import isPrime

def pfactors(n,primes=[2]):
	factors = []
	for i in primes:
		if(n%i==0):
			while(n%i==0): n/=i
			factors.append(i)
			isprime = isPrime(n)
			if isprime and (not n in factors): factors.append(n)
			if(n==1 or isprime): return factors
			break
	if n!=1:
		for i in xrange(primes[len(primes)-1],n):
			ifprime = True
			for j in primes:
				if i%j==0:
					ifprime = False
					break
			if ifprime:
				if(n%i==0):
					while(n%i==0): n/=i
					factors.append(i)
					isprime = isPrime(n)
					if isprime and (not n in factors): factors.append(n)
					if(n==1 or isprime): return factors
				if(not i in primes): primes.append(i)

	return factors

if __name__ == "__main__":
	import sys
	print pfactors(int(sys.argv[1])) 
