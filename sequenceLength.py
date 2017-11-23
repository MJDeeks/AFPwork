my_dna = 'ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT'
length_fragment1 = my_dna.find('GAATTC') + 1
length_fragment2 = len(my_dna) - length_fragment1
print(str(length_fragment1))
print(str(length_fragment2))
#used '' after my_dna = 