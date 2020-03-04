#! /usr/bin/env python3
filename = "dna.txt"  #save filename
infile = open(filename, "r") #open content of filename and save as infile
dna_sequence = infile.read() # read content of file and save as dna_sequence
infile.close() # close file
#print(dna_sequence) # check dna_sequence
#print(dna_sequence.upper())
seq_len = len(dna_sequence.upper()) #get the sequence length
#print(seq_len)
a_count = dna_sequence.upper().count('A')
#print("A=",a_count)
g_count = dna_sequence.upper().count('G')
#print("G=",g_count)
c_count = dna_sequence.upper().count('C')
#print("C=",c_count)
t_count = dna_sequence.upper().count('T')
#print("T=", t_count)
a_content = round(((a_count) /seq_len)*100,2)
g_content = round(((g_count) /seq_len)*100,2) 
c_content = round(((c_count) /seq_len)*100,2) 
t_content = round(((t_count) /seq_len)*100,2) 
print("Percent A: " + str(a_content)+"%")
print("Percent G: " + str(g_content)+"%")
print("Percent C: " + str(c_content)+"%")
print("Percent T: " + str(t_content)+"%")
