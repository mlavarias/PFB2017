import sys
import re

#make open dictionary
genedict = {}

#open file
bamfile = open('bowtie2.sam','r')

#go through each line and split at white space, then split gene at carrot. then combine read and genename and set equal to 1 so that each unique read only can be counted once
for line in bamfile:
	splitline =line.split()
	breakline = splitline[2].split('^')
	genecombo = splitline[0]+'*'+breakline[0] #placed star between them so I cna split later
	genedict[genecombo] = 1

#make new dictionary
readdict = {}

#go through old gene dict. 
for genecombo in genedict:
	genelist = genecombo.split('*') #split at star we established prior
	gene1 = genelist[1] #established gene as key
	if gene1 in readdict: #if gene is alread in dictionary, added 1 count
		readdict[gene1] +=1
	else:                 #if gene wasn't in dictionary, set count =1
		readdict[gene1] = 1

print(readdict) 

sorted_ids = sorted(readdict, key=lambda x:readdict[x], reverse=True)
for sorted_id in sorted_ids:
	print('{}\t{}'.format(sorted_id, readdict[sorted_id]))


#	if gene in genedict:
#		genedict[gene] += 1
#	else:
#		genedict[gene] = 1
#print(genedict)
