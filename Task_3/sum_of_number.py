### Задача аналогичная с заданий на 4-ю неделю, поэтому просто скопировал код.
def sum_numerial (a,sum = 0):
    if a < 1:
        return sum
    sum += a % 10
    a = (a - (a % 10)) / 10
    return sum_numerial(a,sum)

def sum_numerial2 (a): # Решенеи задачи с помощью преобразования числа в строку
    i = 0
    sum = 0

    while i < len(str(a)):
        sum += int(str(a)[i])
        i+=1
    return sum

print(sum_numerial(12345))
print(sum_numerial2(12345))