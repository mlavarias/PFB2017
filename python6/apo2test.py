import re
genes = {}
seq = ''
id=''

with open('apo1.fasta','r') as apo:
 for line in apo:
  if '>' in line:
   id = (line.strip())
   genes[id] = seq
  else:
   seq = (line.strip())
   genes[id] += seq
print(genes)
