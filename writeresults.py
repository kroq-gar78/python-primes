#!/usr/bin/env python

# Write the experiments results into a file

import io

def writeresults(test,maxnum,primes):
	f = open(test+"_" + str(maxnum) + ".accuracy",'w')
	f.write(str(primes)+"\n")
