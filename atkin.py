#!/usr/bin/python

# Seive of Atkin
# Optimization of Sieve of Eratosthenes (trial division) for computers
# http://en.wikipedia.org/wiki/Sieve_of_Atkin

import math

def isPrime(n):
	if( n==2 or n==3 or n==5 ): return True
	primes = [2,3,5]
	sieve = [False]*(n+1)
	factor = int(math.sqrt(n))+1
	for i in xrange(1,factor):
		for j in xrange(1,factor):
			x = 4*i**2+j**2
			r = x%12
			if( x <= n ) and ( r==1 or r==5 ):
				sieve[x] = not sieve[x]
			x = 3*i**2+j**2
			r = x%12
			if( x <= n ) and ( r==7 ):
				sieve[x] = not sieve[x]
			if i>j:
				x = 3*i**2-j**2
				r = x%12
				if( x <= n ) and ( r==11 ):
					sieve[x] = not sieve[x]
	for i in xrange(5,factor):
		if sieve[i]:
			for j in xrange(i**2 , n , i**2):
				sieve[j] = False
	for i in xrange(7,factor):
		if sieve[i]: primes.append(i)
	return primes
	
if __name__ == "__main__":
	import sys
	print isPrime(int(sys.argv[1])) 
