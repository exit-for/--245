def is_symmetric(m):
    n = len(m)  
    for i in range(n):
        for j in range(n):
            if m[i][j] != m[j][i]:  
                return False  
    return True  

# Пример использования
n = int(input("Введите размерность квадратной матрицы: "))
m = []

print("Введите элементы матрицы построчно (через пробел):")
for i in range(n):
    row = list(map(int, input().split()))
    m.append(row)

if is_symmetric(m):
    print("Матрица симметрична.")
else:
    print("Матрица не симметрична.")
