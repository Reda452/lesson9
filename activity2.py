unit=int(input("enter the units that you have used"))
if unit<50:
    amount=unit*2.6
    s=25
elif unit<=100:
    amount = 130 + ((unit - 50) * 3.25)
    s = 35 
elif unit<=200:
    amount = 130 + 162.50 + ((unit - 100) * 5.26)
    s = 45
else:
    amount = 130 + 162.50 + 526 + ((unit - 200) * 8.45)
    s= 75
total=amount+s
print(total)