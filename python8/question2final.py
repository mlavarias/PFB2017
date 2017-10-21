import re
genes = {}
seq = ''
id = ''
codon_frame = open('codons.fasta', 'w')

with open('py8.fasta','r') as dna:
 for line in dna:
  if '>' in line:
   id = (line.strip())
   genes[id] = seq
  else:
   seq = (line.strip())
   genes[id] += seq
for codons in genes:
    codon = re.findall(r"(.{3})",genes[codons])
    genes[codons] = codon
    
    for sing in codon:
     codon_frame.write(codons+'\n'+sing+'\n')
