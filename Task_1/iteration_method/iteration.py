import math


def equation(x):  # Функция в которой задаётся уравнение(функиця f(х) вида: e^-x - 1/2 sin^2x = 0)
    result = math.exp(-x) - 1 / 2 * math.pow(math.sin(x), 2)
    return result


def iteration(x,b):  # Функция метода итераций
    result = x + b*equation(x)
    return result



d_exit = 0.000001
b = 0.8   # Коэффициент b в итерационной формуле
x_k0 = 1  # Начальное приближение к корню
i = 0  # Cчётчик количества итераций
i_max = 20  # Максимальное количество итераций
x_k1 = iteration(x_k0, b)
d = x_k1 - x_k0

if d < d_exit:
    print('Выберите другое начальное приближение')
else:
    while d > d_exit:
        d = x_k1 - x_k0
        x_k0 = x_k1
        x_k1 = iteration(x_k1, b)
        i += 1
        if i >= i_max:
            print('Превышено максимальное количество итераций')
            break

    print('Корень нашего уравнения = %f при заданной точности = %f за количество итераций = %i' % (x_k1, d_exit, i))
    print('При подстановки нашего корня получим')
    print(equation(x_k1))

