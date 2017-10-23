import re
import sys
import numpy
count = 0
length = 0


test = open("fastq.fastq", 'r')
for line in test:
	if line.startswith('@D0'):
		count +=1
	elif line.startswith('+'):
		continue
	elif not re.search(r'^[ACTGN]', line):
		continue
	else:
		length += len(line)
		
	
stddev = numpy.std(length)
print(stddev)
print(count)
print(length/count)
