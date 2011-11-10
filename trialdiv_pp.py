#!/usr/bin/python

import sys
import pp
from trialdiv import isPrime

args = range(int(sys.argv[1]),int(sys.argv[2])+1)

job_server = pp.Server() # uses num. of processors in system
print "Starting pp with", job_server.get_ncpus(), "workers"

#jobs = []
#jobs.append( job_server.submit(isPrime,(args[0],args[1],),(),("math",)) )
#jobs.append( job_server.submit(isPrime,(args[2],args[3],),(),("math",)) )

jobs = [(input,job_server.submit(isPrime , (input,), (), ("math",))) for input in args ]
for input, job in jobs:
	print input , "is" , job()
