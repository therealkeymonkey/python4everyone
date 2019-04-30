import re
fname = input("Enter file name: ")
if not len(fname):
    fname = "regex_sum.txt"
fh = open(fname)
#for line in fh.readline():
#print(fh.read())
numbers = list()
for line in fh:
    num = re.findall('([0-9]+)', line)
    numbers = numbers + num
#print(num_list)
sum = 0
for x in numbers:
    sum = sum + int(x)
print(sum)
