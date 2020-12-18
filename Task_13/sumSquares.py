def sum(N):
    res = 1
    for i in range(1,N + 1):
        res += (2*i - 1)
        print(2*i - 1)
    return round(res - 1, 3)

print('Введите количество слагаемых')
N = int(input())

print('Результат: %i' % (sum(N)))