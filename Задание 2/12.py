import math
import numexpr as ne
x=float(input("Введите переменную x:"))
y=float(input("Введите переменную y:"))
z=ne.evaluate(input("Введите переменную z:"))
s=2**(y**x)+(3**x)**y-((y*(math.atan(z)-1/3))/(abs(x)+((1)/(y**2+1))))
print("s={0:.5f}".format(s))
