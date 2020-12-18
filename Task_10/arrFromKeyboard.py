arr = []
sum = 0

for i in range(0, 5):
    print('a[', i, '] =')
    b = int(input())
    arr.append(b)
    if b != 0:
        s = sum + 1


print('Ненулевых элементов: ', sum)
