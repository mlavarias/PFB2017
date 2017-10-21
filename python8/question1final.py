genes = {}
seq = ''
id = ''


with open('py8.fasta','r') as dna:
 for line in dna:
  if '>' in line:
   id = (line.strip())
   genes[id] = seq
  else:
   seq = (line.strip())
   genes[id] += seq
for dnacount in genes:
    Acount = genes[dnacount].count('A')
    Tcount = genes[dnacount].count('T')
    Ccount = genes[dnacount].count('C')
    Gcount = genes[dnacount].count('G')
    print('seq', dnacount,'A content is:', Acount,'T content is:', Tcount,'C content is:', Ccount,'G content is:',Gcount)
