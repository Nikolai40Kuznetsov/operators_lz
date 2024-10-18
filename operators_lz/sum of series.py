# Импортируем библиотеку
L = float(input("Введите стартовое значение ряда\n"))
S = float(input("Введите конечное значение ряда\n"))
ε = float(input("Введите точность\n"))
sum = 0
n = 1
counter = 0
while sum + L < S:
    sum += 1 / (n * n)
    n += 1
    counter += 1
if sum + L >= S:
    print("Число итераций равно:", counter)