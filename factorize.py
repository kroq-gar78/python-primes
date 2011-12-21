#!/usr/bin/python

import math

def factorize(n,primes=[2]):
	#primes = [2]
	factors = []
	factor = 0
	for i in primes:
		if(n%i==0):
			factor=i
			#print "Number found: %d" % factor
			break
	for i in xrange(primes[len(primes)-1],int(math.sqrt(n))+1):
		ifprime = True
		for j in primes:
			if i%j == 0:
				ifprime = False
				break
		if ifprime:
			#print i
			if(n%i==0):
				factor=i
				#print "Number found: %d" % factor
				break
			if(not i in primes): primes.append(i)
	if factor==0: return [(n,1)]
			
	exp=0
	#tmpn=n
	#print tmpfactor
	while(n%factor==0):
		exp=exp+1
		#print exp
		n=n/factor
		#print tmpfactor
		#if(n<1): break
	#n=n*factor
	#print n
	factors.append((factor,exp))
	#otherfactor=n/(factor**exp)
	#print otherfactor
	if(n!=factor and n!=1):
		results=factorize(n)
		for i in results:
			factors.append(i)
	return factors

if __name__ == "__main__":
	import sys
	print factorize(int(sys.argv[1])) 
