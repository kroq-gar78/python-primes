#!/usr/bin/python

import sys
import pp
from fermat import isPrime
from writeresults import writeresults

def batch(start,end,k=2,bases=[]):
	primesFound = 0
	if bases==[]:
		for n in xrange(start,end):
			if(isPrime(n,k)): primesFound+=1
	else:
		for n in xrange(start,end):
			if(isPrime(n,bases=bases)): primesFound+=1
	return primesFound

ppservers = ()

job_server = pp.Server(ppservers=ppservers) # uses num. of processors in system
jobs = []

rangeStart = (int(sys.argv[1]))
rangeEnd = (int(sys.argv[2]))

primesFound = 0
numJobs = (rangeEnd-rangeStart+1)
#print "Number of jobs:" , numJobs
if numJobs >= 500000: jobsPerBatch = 1<<14 # amount of jobs per batch
elif numJobs >= 100000: jobsPerBatch = 1<<12
else:
	jobsPerBatch = 1<<10
jobsInExtraBatch = numJobs%jobsPerBatch
#print "Jobs in extra batch: " + str(jobsInExtraBatch)
#print "Start of extra batch: " + str(rangeStart)
#print "End of extra batch: " + str(rangeStart+jobsInExtraBatch)
numJobs -= jobsInExtraBatch # remove the modulo just for simplicity
batchesSent = 0 # amount of batches sent EXCLUDING extra batch
# first do the extra batch to reduce the complexity of code
if jobsInExtraBatch != 0:
	jobs.append( job_server.submit(batch , (rangeStart,rangeStart+jobsInExtraBatch,int(sys.argv[3]),), (expmod,isPrime,), ("random",)) )
	#print "Extra:" , rangeStart , rangeStart+jobsInExtraBatch

if numJobs <= 0:
	for job in jobs:
		primesFound+=int(job())
	#print "No more batches needed."
	writeresults("fermat",str(rangeStart)+"to"+str(rangeEnd)+"_b"+sys.argv[3],int(primesFound))
	exit()

batchRangeStart = 0
if jobsInExtraBatch == 0:
	batchRangeStart = rangeStart
else:
	batchRangeStart = rangeStart+jobsInExtraBatch
batchRangeEnd = batchRangeStart+jobsPerBatch
if batchRangeEnd > rangeEnd: batchRangeEnd = rangeEnd
#print "Start of batch 1:" , batchRangeStart
#print "End of batch 1:" , batchRangeEnd
jobs.append( job_server.submit(batch , (batchRangeStart,batchRangeEnd,int(sys.argv[3]),), (isPrime,), ("random",)) )
batchesSent=1

print "Amount of batches:" , numJobs/jobsPerBatch

while (batchesSent*jobsPerBatch) < numJobs:
	
	batchRangeStart = batchRangeEnd
	batchRangeEnd = batchRangeStart+jobsPerBatch
	#print str("Start of batch %d:" % int(batchesSent+1)) , batchRangeStart
	#print str("End of batch %d:" % int(batchesSent+1)) , batchRangeEnd
	#print "\n"
	jobs.append( job_server.submit(batch , (batchRangeStart,batchRangeEnd,int(sys.argv[3]),), (isPrime,), ("random",)) )

	batchesSent+=1

for job in jobs:
	primesFound+=int(job())
	
job_server.print_stats()

writeresults("fermat",str(rangeStart)+"to"+str(rangeEnd)+"_b"+sys.argv[3],int(primesFound))
