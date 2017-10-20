import re
genes = {}
#cutseq = {}
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
for id,cut in genes.items():
  cutsite = re.findall(r'([AG]AATT[CT])', cut)
  print(cutsite)
  cutseq = re.sub(r'([AG])(AATT[CT])',r'\1^\2', cut)
  print(cutseq)
  bigcut = cutseq.split('^')
  sortcut = sorted(bigcut,key=len,reverse=True)
print(sortcut)
