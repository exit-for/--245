def kekw(matrix):
    max_value = float('-inf')
    max_row, max_col = 0, 0
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
                max_row, max_col = i, j

    matrix[0], matrix[max_row] = matrix[max_row], matrix[0]

    for i in range(len(matrix)):
        matrix[i][0], matrix[i][max_col] = matrix[i][max_col], matrix[i][0]

    return matrix

# Пример использования
n = int(input("Введите количество строк матрицы: "))
m = int(input("Введите количество столбцов матрицы: "))
matrix = []

print("Введите элементы матрицы построчно (через пробел):")
for i in range(n):
    row = list(map(float, input().split()))
    matrix.append(row)

print("Исходная матрица:")
for row in matrix:
    print(row)

result_matrix = kekw(matrix)

print("Матрица после перемещения максимального элемента:")
for row in result_matrix:
    print(row)
