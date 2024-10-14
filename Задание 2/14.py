import math
import numexpr as ne
x=ne.evaluate(input("Введите переменную x:"))
y=float(input("Введите переменную y:"))
z=ne.evaluate(input("Введите переменную z:"))
s=((y**(x+1))/(math.pow(abs(y-2),1/3)+3))+((x+y/2)/(2*abs(x+y)))*(x+1)**(-1/math.sin(z))
print("s={0:.4f}".format(s))
