import math
import numexpr as ne

x=ne.evaluate(input("Введите переменную x  :"))
y=float(input("Введите переменную y  :"))
z=ne.evaluate(input("Введите переменную z  :"))
s=abs(x**(y/x)-math.pow(y/x,1/3))+(y-x)*((math.cos(y)-((z)/(y-x)))/(1+(y-x)**2))

print("s={0:.5f}".format(s))
