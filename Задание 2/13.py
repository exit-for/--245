import math
import numexpr as ne
x=float(input("Введите переменную x:"))
y=ne.evaluate(input("Введите переменную y:"))
z=ne.evaluate(input("Введите переменную z:"))
s=(math.pow(y+math.pow(x-1,1/3),1/4)/(abs(x-y)*(math.sin(z)**2+math.tan(z))))
print("s={0:.6f}".format(s))
