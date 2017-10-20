import re
with open('apo1.fasta','r') as apo:
 for line in apo:
  cutsite = re.sub(r'([AG]AATT[CT])', cutsite.group(1), line)
  print(cutsite)
