def multiple(N):
    res = 1
    current = 1.1
    for i in range(0, N):
        res *= current
        current += 0.1
    return round(res, 3)
print('Введите количество множителей, которые надо перемножить')
n = int(input())
print(multiple(n))