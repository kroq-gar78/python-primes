#!/usr/bin/env python

# Parallel Python implementation of trial division

import sys
import pp
from trialdiv import trialdiv
from writeresults import writeresults

if len(sys.argv) < 3:
	print "Not enough arguments supplied. Correct usage is:"
	print "trialdiv_pp.py start-number end-number"
	exit(1)

args = xrange(int(sys.argv[1]),int(sys.argv[2])+1)

ppservers=()

job_server = pp.Server(ppservers=ppservers) # uses num. of processors in system

print job_server.get_active_nodes()

primesFound = 0

jobs = [(num,job_server.submit(trialdiv , (num,), (), ("math",))) for num in args ]
for num, job in jobs:
	#print num , "is" , job()
	if (job() == True):
		primesFound += 1

writeresults("trialdiv",int(sys.argv[2])-int(sys.argv[1])+1,int(primesFound))
