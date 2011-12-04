#!/usr/bin/python

# Seive of Atkin
# Optimization of Sieve of Eratosthenes (trial division) for computers
# http://en.wikipedia.org/wiki/Sieve_of_Atkin

import math
import sys

def isPrime(n):
	if( n==2 or n==3 or n==5 ): return True
	primes = [2,3,5]
	sieve = range(1,int(math.sqrt(n)))
	for i in sieve:
		r=i%60
		netChange = False
		if(r==1 or r==13 or r==17 or r==29 or r==37 or r==41 or r==49 or r==53):
			for x in xrange(1,int(math.sqrt(n))):
				for y in xrange(1,int(math.sqrt(n))):
					if 4*(x>>1)+y>>1 == n: netChange = not netChange
		elif(r==7 or r==19 or r==31 or r==43):
			for x in xrange(1,int(math.sqrt(n))):
				for y in xrange(1,int(math.sqrt(n))):
					if 3*(x>>1)+y>>1 == n: netChange = not netChange
		elif(r==11 or r==23 or r==47 or r==59):
			for x in xrange(1,int(math.sqrt(n))):
				for y in xrange(1,int(math.sqrt(n))):
					if(x>y and 3*(x>>1)-y>>1 == n): not netChange
		if( not netChange ): sieve.remove(i)
	for i in sieve:
		print i
		primes.append(i)
		if n%i==0: return False
		squared = i**2
		for j in sieve:
			if j==squared: sieve.remove(j)
			
	return True

if __name__ == "__main__":
	print isPrime(int(sys.argv[1])) 
