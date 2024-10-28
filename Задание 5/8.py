mc = 0 
cc = 0 
pn = None  
while True: 
    n = int(input("Введите натуральное число (0 для завершения): "))
    if n == 0: 
        break    
    if n == pn:  
        cc += 1
    else:
        mc = max(mc, cc)  
        cc = 1    
    pn = n
mc = max(mc, cc)
print(f"Наибольшее количество подряд идущих одинаковых элементов: {mc}")
