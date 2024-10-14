import math
import numexpr as ne
x=float(input("Введите переменную x:"))
y=ne.evaluate(input("Введите переменную y:"))
z=ne.evaluate(input("Введите переменную z:"))
s=((math.pow(9+(x-y)**2,1/3))/(x**2+y**2+2))-math.exp(abs(x-y))*math.tan(z)**3
print("s={0:.5f}".format(s))
