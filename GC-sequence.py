#this is the sequence to count
mySequence='ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT'

#count the number of C in sequence
numC = mySequence.count('C')
print(numC)

#count the number of G in sequence
numG = mySequence.count('G')
print(numG)

#calculate total number of letters in sequence
total = len(mySequence)
print(total)

#calculate percentage
per = (numC + numG)/total *100
print(per)

#the format method allows me to format the float with any number of decimal
#places. I can easily add more placeholders and variables
print(round(per, 2))
print(round(per, 1))
