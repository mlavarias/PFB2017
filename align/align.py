import sys
import re

#populate dictionary key
field_names = ('qseqid', 'sseqid', 'percid', 'alen', 'mismat', 'gaps', 'q_start', 'q_end', 's_start', 's_end', 'evalue', 'bits')

#open data file in command line
data = open(sys.argv[1],'r')

#make open dictionary
dictdata = {}

#ignores lines that start with # and populates dictionary with field_names key and line ID
for line in data:
	line.strip()
	if line.startswith('#'):
		continue
	else:
		#seq = line.split('\t')
		#for seqline in seq:
		this_data=dict(zip(field_names, line.split('\t')))
		dictdata[field_names] = line
print(this_data)
	

	
