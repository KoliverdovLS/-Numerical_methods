import math


def equation(x):  # Функция в которой задаётся уравнение(функиця f(х) вида: e^-x - 1/2 sin^2x = 0)
    result = math.exp(-x) - 1 / 2 * math.pow(math.sin(x), 2)
    return result


def diff_eduation(x):  # Задаём производную нашего уравнения (Можно было её расчитать с помощью библеотеки "sympu" но я посчитал на листочке и задал сам, что бы для проверки данного задания не приходилось скачивать сторонние библеотеки)
    result = -math.exp(-x) - math.cos(x)
    return result


def newton(x):  # Вычисление следующего значения итерации методот Ньютона
    x_k1 = x - (equation(x) / diff_eduation(x))
    return x_k1


d = 10
d_exit = 0.000001
x_k0 = 0.8  # Начальное приближение к корню
i = 0  # Количество итераций
x_k1 = newton(x_k0)

while d > d_exit:
    d = x_k1 - x_k0
    x_k0 = x_k1
    x_k1 = newton(x_k1)
    i += 1

print('Корень нашего уравнения = %f при заданной точности = %f за количество итераций = %i' % (x_k1, d_exit, i))
print('При подстановки нашего корня получим')
print(equation(x_k1))
