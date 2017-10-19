genesrev = {} #creating empy dictionaries
genes = {}
seq = ''
id = ''

#open fasta file and sorted by seqname and seq
with open('diff.fasta','r') as dna: 
 for line in dna:
  if '>' in line:
   id = (line.strip())
   genes[id] = seq
  else:
   seq = (line.strip())
   genes[id] += seq
for line in genes:
 comp = (genes[line].replace('A', 't').replace ('T', 'a').replace ('C', 'g').replace ('G', 'c'))
 compu = comp.upper()
 revcomp = compu[::-1]
 genesrev[line] = revcomp
print(genesrev)

