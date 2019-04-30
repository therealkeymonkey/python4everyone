fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if word not in lst:
            #print(word)
            lst.append(word)
        #print(lst)
lst.sort()
print(lst)
