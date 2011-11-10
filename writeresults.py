#!/usr/bin/python

import io

def writeresults(test,trial,primes):
	f = open(test+"_trial" + str(trial) + ".accuracy",'w')
	f.write(str(primes)+"\n")
