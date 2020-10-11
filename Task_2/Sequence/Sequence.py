import math


def sum_sequence1(n):
    i = 1
    result = 0
    while i <= n:
        result += 2 * i - 1
        i += 1
    return result

def sum_sequence2(n):
    i = 1
    result = 0
    while i <= n:
        result += 2 ** i - 1
        i += 1
    return result

def sum_sequence3(n):
    i = 1
    result = 0
    while i <= n:
        result += i ** 3 + 1
        i += 1
    return result


print('Выбирите последовательность и введите номер, соответствующий нужной последовательности: \n 1 : 2n-1 \n 2 : '
      '2^n-1 \n 3 : n^3 + 1')
sequence = str(input())

if 1 > int(sequence) > 3:
    print('Error')
else:
    print('Введите n для вывода суммы элементов данной последовательности от 1 до n:')
    n = int(input())

    if n < 1:
        print('Error')
    else:
        if sequence == '1':
            print('Результат: %i' % (sum_sequence1(n)))
        elif sequence == '2':
            print('Результат: %i' % (sum_sequence2(n)))
        elif sequence == '3':
            print('Результат: %i' % (sum_sequence3(n)))



