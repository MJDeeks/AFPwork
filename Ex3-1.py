#open files
inFile = open('/Users/18dbrennan-rasmussen/Downloads/ex3-1_input.txt', 'r')
outFile = open('trim.txt.', 'w')

#trim, add line to fine, print length of line
for line in inFile:
    line = line[14:]
    outfile = outFile.write(line)
    print('line is', len(line), "characters long")
    print(line)

#close files
outFile.close()
inFile.close()