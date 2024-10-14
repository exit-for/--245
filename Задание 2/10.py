import math
import numexpr as ne
x=ne.evaluate(input("Введите переменную x:"))
y=ne.evaluate(input("Введите переменную y:"))
z=float(input("Введите переменную z:"))
s=2**(-x)*math.sqrt(x+(math.pow(abs(y),1/4)))*(math.pow(math.exp(x-1/math.sin(z)),1/3))
print("s={0:.5f}".format(s))
