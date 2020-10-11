


def calculateS_n(n):
    s = 1 / 100
    i = 99
    while i >= n:
        s_previous = 1 / (i + s)
        s = s_previous
        i -= 1
    return s

print('Введите N')
n = int(input())
print(calculateS_n(n))


