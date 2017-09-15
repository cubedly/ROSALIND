f = open ('read.txt', 'r')

dna = f.read()
f.close()

rna = []

for dntp in dna:
    if dntp == 'T': #Remember to use == for equate
        rna.append ('U') #.append add to the end of list
    else:
        rna.append (dntp)

rnastr = ''.join(rna) #Convert a list to a string

print rnastr