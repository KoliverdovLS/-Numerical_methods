import math

n = int(input())
X = []
Y = []

for i in range(0, n + 1):
    X.append(float(input()))
    Y.append(float(input()))

S1 = 0
S2 = 0
S3 = 0
S4 = 0

for i in range(0, n + 1):
    S1 = S1 + Y[i]
    S2 = S2 + X[i]
    S3 = S3 + X[i] * Y[i]
    S4 = S4 + pow(X[i], 2)

D = S4 * (n + 1) - pow(S2, 2)
a0 = (S1 * S4 - S2 * S3) / D
a1 = ((n + 1) * S3 - S2 * S1) / D
print('Y =', a0, '+', a1, '* X')
S = 0

for i in range(0, n + 1):
    S = S + float(pow((a0 + a1 * X[i] - Y[i]), 2))

D = float(math.sqrt(S / n))

print('сумма квадрат отклонений S =', S, '; дисперсия D =', D)
print('Хотите сравнить исходные данные с расчетными?')
O = str(input())

if O == 'да':
    for i in range(1, n + 1):

        Yp = a0 + a1 * X[i]
        print('X[', i, '] =', X[i])
        print('Y[', i, '] =', Y[i])
        print('Yp =', Yp)
        print('(Yp-Y[', i, '])/Y[', i, '] =', float((Yp - Y[i]) / Y[i]))

    else:
        print('Считать приближенные значения функции?')
        O = str(input())

        if O == 'да':
            Xp = float(input())
            Yp = a0 + a1 * Xp
            print('Xp =', Xp, '\tYp =', Yp)
