import sys
import re
genes = {}
id = ''
seq = ''
class invalidseq(Exception):
	pass

try:
	file = sys.argv[1]
	print('fasta provided', file)

	if not file.endswith('.fa') or not file.endswith('.fasta') or not file.endswith('.nt'):
		raise ValueError('Not a valid file format')

	for line in dna:
		if '>' in line:
			id = (line.strip())
			genes[id] = seq
	else:
		seq = (line.strip())
		genes[id] += seq
		if re.search('[^ATGCN]+', genes(id)):
			raise invalidseq('not found in seq')
except IndexError:
	print('No file given')
except IOError:
	print('Cannot find file')
except ValueError:
	print('Invalid file format')
except invalidseq:
	print('Nucleotides not found in seq')
