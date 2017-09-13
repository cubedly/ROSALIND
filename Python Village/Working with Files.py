f = open('read.txt','r')

list_file = []

i = 1

for line in f:
    if i % 2 == 0:
        list_file.append(line)
    i = i + 1

f.close()

print list_file

f=open('write.txt','a')
for x in list_file:
    f.write(x)

f.close()