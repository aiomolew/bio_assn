#! /usr/bin/env python3

# define an input file 
infile = 'watermelon.gff'

# Create an emptylist gene_name
gene_name =[]
# Read file and parse
with open(infile, 'r') as watermelon:
    for line in watermelon:
        # split each line into field using tab as the separator
        fields = line.split("\t")
        # extract the line that contains the gene name and split it using ; as the seperator
        gene_field = fields[8].split(';')
        # extract the gene name section and split using space as the separator
        gene_name_field = gene_field[0].split(' ')
        # save the gene name in a list while skiping the "similar"        
        if gene_name_field[1] != 'similar':
            gene_name.append(gene_name_field[1])
        
sorted_gene_name = sorted(gene_name)
print(sorted_gene_name)
