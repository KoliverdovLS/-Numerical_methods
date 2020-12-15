def isEven(num):
    if (num % 2 == 0):
        print('%i - четное' % (num))
    else:
        print('%i - нечетное' % (num))
    return


print("Вычисление четности \n Введите число:")
num = int(input())
isEven(num)