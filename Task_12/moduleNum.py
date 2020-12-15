def moduleNumber(num):
    return abs(num)

print("Вычисление модуля числа \n Введите число:")
num = int(input())
print('Модуль числа от %i равен: %i' % (num, moduleNumber(num)))
