def minutesInHours(min):
    minutes = min % 60
    hours = (min - minutes) / 60
    print("%i ч. %i мин." % (hours, minutes))
    return
print("Вычисление времени \n Введите минуты:")
min = int(input())
minutesInHours(min)