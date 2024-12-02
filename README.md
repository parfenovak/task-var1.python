В файле .py реализуется ввод из терминала. 

Версия с вводом в коде:
def print_numbers(A, B):
    if A > B:
        print("Ошибка: A должно быть меньше или равно B")
        return
    if A == B:
        print("Числа А и В равны")
        return
    
    for number in range(A, B + 1):
        print(number)
A = 3
B = 7
print_numbers(A, B)
