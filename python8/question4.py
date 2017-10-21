import re
genes = {}
seq = ''
id = ''
frames = open('frames.fasta', 'w')

with open('test8.fasta','r') as dna:
 for line in dna:
  if '>' in line:
   id = (line.strip())
   genes[id] = seq
  else:
   seq = (line.strip())
   genes[id] += seq
for codons in genes:
    codon = re.findall(r"(.{9})",genes[codons])
    #for splitting in codon:
     
    genes[codons] = codon
    print(codons,codon)    
