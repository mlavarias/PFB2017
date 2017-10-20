import re
line_count = 0
print('start','end', 'line', sep='\t')
with open("silver.txt",'r') as silver:
 for poem in silver:
  line_count +=1
  for match in re.finditer("Nobody", poem):
   print(match.start(), match.end(), line_count, sep='\t')
