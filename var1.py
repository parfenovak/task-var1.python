def print_numbers(A, B):
    if A > B:
        print("Ошибка: A должно быть меньше или равно B")
        return
    
    if A == B:
        print("Числа А и В равны")
        return
    
    for number in range(A, B + 1):
        print(number)

A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

print_numbers(A, B)
