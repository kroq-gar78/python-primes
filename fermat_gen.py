#!/usr/bin/python

import sys, time
from fermat import isPrime

args = range(int(sys.argv[1]),int(sys.argv[2])+1)

start = time.time()

for num in args:
	isPrime(num)

print "Time elapsed:" , time.time()-start
