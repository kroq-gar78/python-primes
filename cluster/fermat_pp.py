#!/usr/bin/python

import sys
import pp
from expmod import expmod
from fermat import isPrime
from writeresults import writeresults

def batch(start,end,k=2,bases=[]):
	primesFound = 0
	if bases==[]:
		for i in xrange(start,end):
			if(isPrime(n,k): primesFound+=1
	else:
		for i in xrange(start,end):
			if(isPrime(n,bases=bases)): primesFound+=1

args = xrange(int(sys.argv[1]),int(sys.argv[2])+1)

ppservers = ()

job_server = pp.Server(ppservers=ppservers) # uses num. of processors in system
jobs = []

print job_server.get_active_nodes()

rangeStart = (int(sys.argv[1]))
rangeEnd = (int(sys.argv[2]))

primesFound = 0
numJobs = (rangeStart-rangeEnd+1)
jobsPerBatch = 1<<10 # amount of jobs per batch
jobsInExtraBatch = numJobs%jobsPerBatch
batchesSent = 0
# first do the extra batch to reduce the complexity of code
if jobsInExtraBatch != 0:
	jobs.append( job_server.submit(batch , (rangeStart,rangeStart+jobsInExtraBatch,int(sys.argv[3]),), (expmod,isPrime,), ("random",)) )
#while batchesSent*jobsPerBatch+jobsInExtraBatch < (int

writeresults("fermat",int(sys.argv[2])-int(sys.argv[1])+1,int(primesFound))
