import math
import numexpr as ne
x=float(input("Введите переменную x:"))
y=float(input("Введите переменную y:"))
z=float(input("Введите переменную z:"))
s=y**math.pow(abs(x),1/3)+math.cos(y)**3*((abs(x-y)*(1+((math.sin(z)**2)/(math.sqrt(x+y))))/(math.exp(abs(x-y)+x/2))))
print("s={0:.6f}".format(s))
