import re
with open("silver.txt",'r') as silver:
 for poem in silver:
  nobody=re.sub(r'Nobody','Mitchell',poem)
 
