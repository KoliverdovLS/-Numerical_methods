

#Парабола
def f(x):
    return x * 2 - 3 * x - 15


 # Задаём производную нашего уравнения (Можно было её расчитать с помощью библеотеки "sympu" но я посчитал на листочке и задал сам, что бы для проверки данного задания не приходилось скачивать сторонние библеотеки)
def df(x):
    return 2 * x - 3


x0 = -5  # Начальное приближение к корню
d = 0  # Итерации
h = 0.1  #Шаг


while d < 100:
    x0 -= h * df(x0)

    d += 1
    print(x0,'---', f(x0))


