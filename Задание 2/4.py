import math
import numexpr as ne
x=ne.evaluate(input("Введите переменную x:"))
y=float(input("Введите переменную y:"))
z=ne.evaluate(input("Введите переменную z:"))
s=abs(math.cos(x)-math.cos(y))**(1+2*math.sin(y)**2)*(1+z+z**2/2+z**3/3+z**4/4)
print("s={0:.5f}".format(s))
