name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
times = list()
hours = list()
lst = list()
# Build a list of addresses
for line in handle:
    line = line.rstrip()
    if not line.startswith('From '): continue
    addys = line.split()
# Pull times from list
    times.append(addys[5])
# Isolate hour
for line in times:
    hour = line.split(':')
    #print(hour)
    hours.append(hour[0])
# Count the number of unique hours and print the list
for h in hours:
    counts[h] = counts.get(h,0) +1
counts = sorted ( [ (k,v) for k,v in counts.items() ] )
for key, val in counts:
    print(key, val)
