import math
import numexpr as ne

x=float(input("Введите переменную x  :"))
y=ne.evaluate(input("Введите переменную y  :"))
z=int(input("Введите переменную z  :"))
s=math.log10(y**(-(math.sqrt(abs(x)))))*(x-(y/2))+math.sin(math.atan(z))**2

print("s={0:.5f}".format(s))
