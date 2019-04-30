name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
names = list()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From '): continue
    addys = line.split()
    #names = addys[1]
    names.append(addys[1])
#print(names)
for line in names:
    counts[line] = counts.get(line,0) +1
#print(counts)

spammer = None
offences = None
for mail,count in counts.items():
    if offences is None or count > offences:
        spammer = mail
        offences = count
print(spammer, offences)
