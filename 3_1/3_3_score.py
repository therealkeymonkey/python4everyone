scr = input("Enter Score between 0.0 and 1.0:")
try:
    scr = float(scr)
except:
    print("ERROR:Enter a numeric score")
    quit()
if scr < 0.0:
    print("ERROR:Enter score within range")
elif scr > 1.0:
    print("ERROR:Enter score within range")
elif scr >= 0.9:
    print("A")
elif scr >= 0.8:
    print("B")
elif scr >= 0.7:
    print("C")
elif scr >= 0.6:
    print("D")
else: print("F")
