#!/usr/bin/python

import sys
import pp
from euclidean import gcd
from jacobi import jacobi
from solovaystrassen import isPrime
from writeresults import writeresults

args = range(int(sys.argv[1]),int(sys.argv[2])+1)

ppservers=(,)

job_server = pp.Server(ppservers=ppservers) # uses num. of processors in system

print job_server.get_active_nodes()

primesFound = 0

jobs = [(input,job_server.submit(isPrime , (input,3,), (jacobi,gcd,), ("random",))) for input in args ]
for input, job in jobs:
	#print input , "is" , job()
	if (job() == True):
		primesFound += 1

writeresults("solovaystrassen",args[len(args)-1],int(primesFound))
