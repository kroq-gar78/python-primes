#!/usr/bin/python

import sys
import pp
from fermat import isPrime
from writeresults import writeresults

args = range(int(sys.argv[1]),int(sys.argv[2])+1)

ppservers = ("192.168.1.78",)

job_server = pp.Server(ppservers=ppservers) # uses num. of processors in system
#print "Starting pp with", job_server.get_ncpus(), "workers"

print job_server.get_active_nodes()

#jobs = []
#jobs.append( job_server.submit(isPrime,(args[0],args[1],),(),("math",)) )
#jobs.append( job_server.submit(isPrime,(args[2],args[3],),(),("math",)) )

primesFound = 0

jobs = [(input,job_server.submit(isPrime , (input,3,), (), ("random",))) for input in args ]
for input, job in jobs:
	#print input , "is" , job()
	if( job() == True ):
		primesFound += 1

writeresults("fermat",0,int(primesFound))
