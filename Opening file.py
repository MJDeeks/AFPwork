#open file
dna_file = open("/user/18dbrennan-rasmussen/downloads/geonomic_data.txt")
#read dna from file
dna = dna_file.read()
#close file
dna_file.close()

#extract exons/introns from DNA
exon1 = dna[0:63]
intron = dna[63:90]
exon2 = dna[90:]
#create coding sequence
coding_seq = exon1 + exon2

#create output file
coding_file = open('coding.txt', 'w')
#write coding sequence to file
coding_file.write(coding_seq)
print('Coding file created - coding.txt\n')