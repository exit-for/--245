import math
import numexpr as ne

x=ne.evaluate(input("Введите переменную x  :"))
y=float(input("Введите переменную y  :"))
z=float(input("Введите переменную z  :"))
s=math.sqrt(10*(math.pow(x,1/3)+x**(y+2)))*(math.asin(z)**2-abs(x-y))

print("s={0:.4f}".format(s))
