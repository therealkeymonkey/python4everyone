hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
if h <= 40:
    pay = h * r
    print(pay)
elif h > 40:
    over = h % 40
    pay = (40 * r) + (int(over) * (r * 1.5))
    print(pay)
