#! /usr/bin/env python3
import csv
#specify input file
gff_file ='watermelon.gff'

# Create an emptylist gene_name
gene_names =[]
# Read GFF file line by line
with open(gff_file, 'r') as gff:
	
	# create a csv reader object
	reader = csv.reader(gff, delimiter="\t")
	
	for line in reader:
		#skip blank lines
		if not line:
			continue;
		else:
			print(line[3], line[4])







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
