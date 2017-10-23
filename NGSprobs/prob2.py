import re
import sys
import numpy
count = 0
length = 0
mylist = []


test = open("testfastq.fastq", 'r')
for line in test:
	if line.startswith('@D0'):
		count +=1
	elif line.startswith('+'):
		continue
	elif not re.search(r'^[ACTGN]', line):
		continue
	else:
		length += len(line)
		lengthh = len(line)
		lenstring = str(lengthh)
		mylist += lenstring
		
	
stddev = numpy.std(length)
print(stddev)
print(count)
print(length/count)
print(mylist)
