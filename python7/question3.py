import sys
import re
dna = open(sys.argv[1],'r')
seq_len = int(sys.argv[2])
dna_output = open('fastacut.fasta','w')
nuc = ''
def format_dna(sequence,seq_len):
	new_seq=''
	sequence = re.sub('\n', '', sequence)
	sequence = sequence.strip()
	while sequence:
		if len(sequence) >= seq_len:
			new_seq += sequence[0:seq_len] + '\n'
			sequence = sequence[seq_len:len(sequence)]
		else:
			new_seq += sequence[0:len(sequence)]
			sequence = ''
		return new_seq
for line in dna:
	if '>' in line:
		nuc = line.strip()
		dna_output.write(nuc+'\n')
	else:
		nuc = line.strip()
		nuc += nuc
		new_out = format_dna(nuc, seq_len)
		dna_output.write(new_out)
