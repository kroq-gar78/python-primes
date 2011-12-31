#!/usr/bin/python

import math
	
def factorize(n,primes=[2]):
	factors = {}
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
		exp=+1
		n/=factor
	factors[factor]=exp
	if(n!=factor and n!=1):
		results=factorize(n)
		for i in results.keys():
			factors[i]=results[i]
	return factors

if __name__ == "__main__":
	import sys
	print factorize(int(sys.argv[1])) 
