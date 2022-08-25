import math


pKa1 = float(input("pKa  "))
cb1 = float(input("Concentration of CB:  "))
ca1 = float(input("concentration of CA:  "))
volume = 1
x = pKa1 + math.log10(cb1/ca1)
print(x)
dPH = float(input())conda inc