import math
import numexpr as ne
x=float(input("Введите переменную x:"))
y=ne.evaluate(input("Введите переменную y:"))
z=ne.evaluate(input("Введите переменную z:"))
s=((x**(y+1)+math.exp(y-1))/(1+x*abs(y-math.tan(z))))*(1+abs(y-x))+((abs(y-x)**2)/(2))-((abs(y-x)**3)/(3))
print("s={0:.6f}".format(s))
