import re
line_count = 0
print('start','end', 'line', sep='\t')
silv_read =  open("silver.txt",'r')
silv_write = open('Rex.text','w')
for poem in silv_read:
  rex = re.sub(r'Nobody', r'Rex', poem)
  silv_write.write(rex)
