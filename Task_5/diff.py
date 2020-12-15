import math


def f1(x):  # Функция в которой задаётся уравнение(функиця f(х) вида: e^-x - 1/2 sin^2x = 0)
    return x ** 2 - 3 * x - 15


def df1(x):  # Задаём производную нашего уравнения для сравнения с приближенными методами
    return 2 * x - 3


def df2(x, y): #Ещё одно уравнение для метода Эйлера
    return x ** 2 - 2 * y


def dff(x, h):  # Приближенное вычисление производной
    result = (f1(x + h) - f1(x)) / h
    return result


def diffEuler(x, y, i, h=0.1): #Метод Эйлера
    n = 0
    while n < i:
        y = y + h * df2(x, y)
        x += h
        n += 1
        print("y =", y)

    return 'y = ', y, 'x = ', x, 'df(x,y) = ', df2(x, y)




print('Точная производная--', df1(0.5), 'Приближенная--', dff(0.5, 0.0001))

print("Метод Эйлера")
print(diffEuler(0, 1, 10))
