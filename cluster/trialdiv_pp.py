#!/usr/bin/python

import sys
import pp
from trialdiv import isPrime

args = xrange(int(sys.argv[1]),int(sys.argv[2])+1)

ppservers=(,)

job_server = pp.Server(ppservers=ppservers) # uses num. of processors in system

print job_server.get_active_nodes()

jobs = [(input,job_server.submit(isPrime , (input,), (), ("math",))) for input in args ]
for input, job in jobs:
	print input , "is" , job()
