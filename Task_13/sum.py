def sum(N):
    res = 0
    current = 1.1
    for i in range(0,N):
        res += current
        current += 0.1
        current = (-current) # Что бы не использовать условия, просто меняем знак каждую итерацию
    return round(res, 3)

print('Введите количество слагаемых')
N = int(input())
print(sum(N))