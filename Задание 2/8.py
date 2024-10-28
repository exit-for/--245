import math
import numexpr as ne

x=ne.evaluate(input("Введите переменную x  :"))
y=float(input("Введите переменную y  :"))
z=float(input("Введите переменную z  :"))
s=((math.exp(abs(x-y))*abs(x-y)**(x+y))/(math.atan(x)+math.atan(z)))+math.pow(x**6+math.log10(y)**2,1/3)

print("s={0:.4f}".format(s))
