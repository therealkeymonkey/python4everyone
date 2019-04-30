hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
   h = float(hrs)
   r = float(rate)
except:
    print("ERROR:Enter numeric data")
    quit()

def computepay(h,r):
    if h <= 40:
        pay = h * r
        print(pay)
    elif h > 40:
        over = h % 40
        pay = (40 * r) + ((over) * (r * 1.5))
    return(pay)

p = computepay(h,r)
print("Pay",p)
