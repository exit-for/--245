def reverse_number(n):
    n_str = str(n)
    
    if n_str == "":
        return ""
    return n_str[-1] + reverse_number(n_str[:-1])

# Пример использования
number = int(input("Введите число: "))
reversed_number = reverse_number(number)
print("Число в обратном порядке:", reversed_number)

