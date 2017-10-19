with open ('py5.fastq') as infile:
 lines=0
 words=0
 characters=0
 for line in infile:
  wordslist=line.split()
  lines=lines+1
  words=words+len(wordslist)
  characters += sum(len(word) for word in wordslist)
print('numbers of lines:', lines)
print('numbers of words:', words)
print('numbers of characters:', characters)
avlength = characters/lines
print('average line length:', avlength)
