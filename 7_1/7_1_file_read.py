# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('Sorry, file not found')
    exit()

#print(fname)
fhimp = fh.read()
#print(fhimp)
fhimp = fhimp.rstrip()
caps = fhimp.upper()
print(caps)
