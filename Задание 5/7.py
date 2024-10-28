c = 0  
pn = None  
while True:  
    n = int(input("Введите натуральное число (0 для завершения): ")) 
    if n == 0:  
        break      
    if pn is not None and n > pn:
        c += 1  
    pn = n
print(f"Количество элементов, больших предыдущего: {c}")
