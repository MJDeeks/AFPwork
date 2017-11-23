#part 1
my_dna = 'ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT'
ex1 = my_dna [0:63]
ex2 = my_dna [90:]
print('Original seqence {0} \n'.format(my_dna))
print('Coding ex 1: {0} \nCoding ex 2: {1}'.format(ex1, ex2))
#used [] instead of {}

#part2
coding_length = len(ex1+ex2)
total_length = len(my_dna)
print('{0:.2f}%'.format(coding_length/total_length*100))

#part 3
intron = my_dna[63:90]
print('Original sequence: {0} \n'.format(my_dna))
print("Coding DNA: {0}\nNon Coding DNA: {1}\nCoding DNA: {2}".format(ex1, intron.lower(),ex2))