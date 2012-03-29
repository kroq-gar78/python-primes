#!/usr/bin/python

# Parallel Python implementation of the Lucas-Lehmer Primality Test

import sys
import pp
from lucaslehmer import lucaslehmer
from trialdiv import isPrime
from writeresults import writeresults

args = xrange(int(sys.argv[1]),int(sys.argv[2])+1)

ppservers = ()

job_server = pp.Server(ppservers=ppservers) # uses num. of processors in system

print job_server.get_active_nodes()

primesFound = 0

jobs = [(num,job_server.submit(lucaslehmer , (num,int(sys.argv[3])), (isPrime,), ("random","math"))) for num in args ]
for num, job in jobs:
	#print num , "is" , job()
	if( job() == True ):
		primesFound += 1
		print "M%d"%num,
		sys.stdout.flush()

writeresults("lucaslehmer",int(sys.argv[2])-int(sys.argv[1])+1,int(primesFound))
