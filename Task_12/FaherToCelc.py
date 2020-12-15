def FahrenheitToC(F):
    return (5 / 9) * (F - 32)

print("Вычисление температуры в C \n Введите температуру по Фаренгейту:")
F = int(input())
print('Температура по цельсию - %i' % (FahrenheitToC(F)))
