# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    #print(line)
    count = count + 1
    start = line.find('0')
    #print(start)
    num = line[start - 1:]
    num = float(num)
    total = total + num
    aver = total/count
#print("Done")
print("Average spam confidence:", aver)
