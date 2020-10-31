def calculate_factorial(n):
    if n < 0:
        return 'error'

    if n == 0:
        return 1

    result = 1
    i = 1
    while i < n:
        result += result * i
        i += 1
    return result


print("Вычисление факториала \n Введите число:")
n = int(input())
print('Факториал от %i равен: %i' % (n, calculate_factorial(n)))
