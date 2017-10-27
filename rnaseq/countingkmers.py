import re
import sys
from Bio import SeqIO

kmer_length = 8 
#sys.argv[1]
filename = sys.argv[1]
top_kmers = 10
# sys.argv[3]

kmerdict = {}

def count_kmers(kmerdict, sequence):
	for i in range(0,len(sequence)-kmer_length+1):
		kmer = sequence[i:i+kmer_length]
		if kmer in kmerdict:
			kmerdict[kmer] += 1
		else:
			kmerdict[kmer] = 1	

for record in SeqIO.parse(filename, 'fastq'):
#	print(record.seq)
	count_kmers(kmerdict, str(record.seq))


top_sorted = sorted(kmerdict, key= lambda x:kmerdict[x], reverse = True)[0:top_kmers+1]
for item in top_sorted:
	print('{}\t{}'.format(item, kmerdict[item]))
