# Импортируем библиотеку
import math
input_data = open('input.txt', 'r')
output_data = open('output.txt', 'w')
n = input_data.readline()
i = 2
# Вводим переменную для подсчёта делителей, отличных от 1
flag = 0
# Проводим подсчёт делителей, отличных от 1 
while i <= math.sqrt(int(n)):
	if int(n) % i == 0:
		flag += 1
	i += 1
# Число считается простым, если количество делителей, отличных от 1, равно 0
if flag == 0:
    output_data.write("Y")
# Иначе число составное
else:
	output_data.write("N")
input_data.close()
output_data.close()