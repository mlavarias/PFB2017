import random
dna =list("AAATTGGGCC")
for dnashuffle in dna:
 index1 = random.randrange(len(dna))
 index2 = random.randrange(len(dna))
 dna[index1], dna[index2] = dna[index2], dna[index1]
 #base1 = dna[index1]
 #base2 = dna[index2]
 #dna[index1] = base2
 #dna[index2] = base1
 print(dna)
