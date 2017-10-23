import re
import sys
import numpy
count = 0
length = 0
linenum = 0
seq_qual = []
total_qual = []


test = open("fastq.fastq", 'r')
for line in test:
	lines = line.strip()
	linenum += 1
	if linenum%4 == 1:
		count +=1
	elif linenum%4 == 2:
		length += len(lines)
	elif linenum%4 == 3:
		continue
	elif linenum%4 == 0:
		for qual in lines:
			seq_qual.append(ord(qual)-33)
		total_qual.append(numpy.average(seq_qual))
	#else:
	#	continue
stddev = numpy.std(length)
astddev = numpy.std(seq_qual)
aqual = numpy.average(seq_qual)
print('There is/are',count, 'sequences')
print('The average length is',length/count, 'nucleotides')
print('The standard deviation of nucleotides in the sequence is', stddev)
print('The average quality score is', aqual)
print('The standard deviation of quality score is', astddev)
