import math


def equation(x):  # Функция в которой задаётся уравнение(функиця f(х))
    result = math.exp(-x) - 1 / 2 * math.pow(math.sin(x), 2)
    return result


def chord(a, b):  # Вычисление следующего значения b методом хорд
    result = b - ((a - b) / (equation(a) - equation(b))) * equation(b);
    return result


a = 1  # Задаём интервал [a,b]
b = 1.5

f_a = equation(a)  # Значение f(x) при x=a и x=b
f_b = equation(b)

b1 = (chord(a, b))  # Вычисление следующей итерации приблежения

d = 10  # Переменная в которой будет храниться разница между
d_exit = 0.00001  # Задаём точность (разцину между приближениями при которой цикл вызова функции chord остановится

while d > d_exit:
    b = b1
    b1 = chord(a, b1)
    d = b - b1


print('Корень нашего уравнения = %f при заданной точности = %f' % (b1, d_exit))

