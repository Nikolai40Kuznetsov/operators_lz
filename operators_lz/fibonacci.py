input_data = open('input.txt', 'r')
output_data = open('output.txt', 'w')
n = input_data.readline()
# Вводим значения для двух первых членов последовательности
fib1 = 0
fib2 = 1
# Выводим значения двух первых членов последовательности через запятую
output_data.write(str(fib1))
output_data.write(", ")
output_data.write(str(fib2))
output_data.write(", ")
for i in range(2, int(n) + 1):
    # Переприсваеваем n-ому и n+1-ому члену значения n+1-ого и n+2-ого
    fib1, fib2 = fib2, fib1 + fib2
    # Выводим в файл новое значение переменной fib2 (она сейчас равна n+2-ому члену)
    output_data.write(str(fib2))
    # Расставляем запятые
    if i != (int(n)):
        output_data.write(", ")
input_data.close()
output_data.close()