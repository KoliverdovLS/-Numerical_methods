def CelToFar(t1, t2, dt):
    print('C --- F \n-------')
    i = t1;
    while (i <= t2):
        print('%i --- %i' % (i, ((9/5)*i + 32)))
        i += dt
    return


print("Вычисление температуры \n Введите начальную в цельсиях:")
t1 = int(input())
print("Введите конечную температуру в цельсиях")
t2 = int(input())
print("Введите шаг")
dt = int(input())
CelToFar(t1, t2, dt)
