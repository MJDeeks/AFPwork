#open file
dna_file = open("/user/18dbrennan-rasmussen/desktop/genomic_data.txt", 'r')
#read dna from file
dna = dna_file.read()

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
#save and close
coding_file.close()

#create output file for non-coding sequence
noncoding_file = open('noncoding,txt', 'w')
#write non-coding sequence into file
noncoding_file.write(intron)
print('non coding file - noncoding.txt')
#save andc close
noncoding_forl.close()