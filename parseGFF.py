#! /usr/bin/env python3
import csv
from Bio import SeqIO
import argparse

# create an argument parser object
parser = argparse.ArgumentParser(description = "This script parse GFF and Fasta files and does stuffs with them")

# add positional argument for teh input position in the Fib sequence
parser.add_argument("gff", help="Name of GFF file")
parser.add_argument("fasta", help="Name of the FASTA file")

# parse the arguments
args = parser.parse_args()

#specify input file
gff_file = args.gff
fasta_file =  args.fasta

#read and parse the FASTA file
genome = SeqIO.read(fasta_file, 'fasta')


dna_CDS = ""
# Create an emptylist gene_name
gene_names =[]
# Read GFF file line by line
with open(gff_file, 'r') as gff_input:
	
	# create a csv reader object
	reader = csv.reader(gff_input, delimiter="\t")
	
	for line in reader:
		#skip blank lines
		if not line:
			continue;
		else:
			
			if line[2] == "CDS":
				start = int(line[3])
				end = int(line[4])
				dna_CDS = dna_CDS + genome.seq[start:end]


#print(dna_CDS)

#get the sequence length
seq_len = len(dna_CDS.upper())

#calculate GC content
g_count = dna_CDS.upper().count('G')
c_count = dna_CDS.upper().count('C')

g_c_content = round(((g_count+ c_count) /seq_len)*100,2)

print(g_c_content) 






#    for line in watermelon:
#        # split each line into field using tab as the separator
#        fields = line.split("\t")
#        # extract the line that contains the gene name and split it using ; as the seperator
#        gene_field = fields[8].split(';')
#        # extract the gene name section and split using space as the separator
#        gene_name_field = gene_field[0].split(' ')
#        # save the gene name in a list while skiping the "similar"        
#        if gene_name_field[1] != 'similar':
#            gene_name.append(gene_name_field[1])
        
#sorted_gene_name = sorted(gene_name)
#print(sorted_gene_name)

#for gene in sorted_gene_name:
#	print(gene)
