text = "X-DSPAM-Confidence:    0.8475";
zeropos = text.find('0')
#print(zeropos)
num = text[zeropos-1:]
num = float(num)
print(num)
