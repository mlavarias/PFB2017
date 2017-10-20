import re
with open('py6.fasta','r') as dna:
 for line in dna:
  found = re.search(r'(^>\S+)(\s?.*)', line)
  if found:
   print("id:",found.group(1), 'extracted description:', found.group(2))
