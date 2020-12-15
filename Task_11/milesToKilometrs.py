def mToKm(miles):
    m = 1.6009
    return float(miles * m)

print("Вычисление расстояния в километрах \n Введите мили:")
miles = int(input())
print('Расстояние равно: %i' % (mToKm(miles)))
