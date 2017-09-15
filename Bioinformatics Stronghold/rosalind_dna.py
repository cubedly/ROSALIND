#Rosalind_DNA - Counting DNA nucleotides

f = open ("read.txt","r")

s = f.read() #read returns a string
f.close()

d = {}

for c in s:
    if c in d:
        d[c] = d[c] + 1
    else:
        d[c] = 1
print d["A"], d["C"], d["G"], d["T"]


#Alternate simple solution using .count

print s.count ("A"), s.count ("C"), s.count ("G"), s.count ("T")