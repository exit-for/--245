import math
import numexpr as ne
x=float(input("Введите переменную x  :"))
y=float(input("Введите переменную y:  "))
z=ne.evaluate(input("Введите переменную z  :"))
s=(2 * math.cos(x-2/3))/(1/2 + math.sin(y)**2)*(1 + (( z **2 )/( 3 - z **2 / 5 )))
print("s={0:.5f}".format(s))
