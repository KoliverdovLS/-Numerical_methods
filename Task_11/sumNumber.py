def sumNum():
    print('Обработка последовательности дробных чисел')
    i = 0;
    sum = 0;
    while (i < 5):
        num = float(input())
        sum += num
        i += 1
        print('Введено чисел: %i Сумма: %i' % (i, sum))
    print('Среднее арифметическое: %i' % (sum/i))

sumNum()