#!/usr/bin/python

import sys
import pp
from expmod import expmod
from euclidean import gcd
from jacobi import jacobi
from solovaystrassen import isPrime
from writeresults import writeresults

args = xrange(int(sys.argv[1]),int(sys.argv[2])+1)

ppservers=()

job_server = pp.Server(ppservers=ppservers) # uses num. of processors in system

print job_server.get_active_nodes()

primesFound = 0

jobs = [(num,job_server.submit(isPrime , (num,3,), (jacobi,gcd,expmod,), ("random",))) for num in args ]
for num, job in jobs:
	#print num , "is" , job()
	if (job() == True):
		primesFound += 1

writeresults("solovaystrassen",int(sys.argv[2])-int(sys.argv[1])+1,int(primesFound))
