n = 3
xp = 5
x = [1, 3, 5, 7]
y = [6, 2, 5, 3]
h = []
a = []

for i in range(1, n + 1):
    h.append(x[i] - x[i - 1])
    a.append(y[i - 1])

c = [0 for n in range(n + 1)]
c[1] = 0
c[n + 1] = 0
M = [0 for m in range(n + 1) for nn in range(n + 1)]

for i in range(2, n + 1):
    M[i][i] = 2 * (h[i - 1] + h[i])
    M[i][i - 1] = h[i]
    M[i][i + 1] = h[i]
    M[n + 1] = 3 * ((y[i] - y[i - 1]) / h[i] - (y[i - 1] - y[i - 2]) / h[i - 1])

AA = []
AA.append(M[1][2] / M[1][1])
BB = []
BB.append(M[1][n + 1] / M[1][1])

for i in range(2, n - 1):
    e = M[i][i - 1] * AA[i - 1] + M[i][i]
    AA[i] = -M[i][i + 1] / e
    BB[i] = (M[i][n + 1] - M[i][i - 1] * BB[i - 1]) / e

C = [0 for y in range(n + 1)]
C[n] = (M[n][n + 1] - M[n][n - 1] * BB[n - 1]) / (M[n][n] + M[n][n - 1] * AA[n - 1])
i = n

while i > 2:
    i = i - 1
    C[i] = AA[i] * C[i + 1] + BB[i]

b = [0 for t in range(n + 1)]
b[n] = (y[n] - y[n - 1]) / h[n] - 2 / 3 * h[n] * C[n]
d = [0 for t in range(n + 1)]
d[n] = -c[n] / (3 * h[n])

for i in range(1, n):
    b[i] = (y[i] - y[i - 1]) / h[i] - (h[i] * (C[i + 1] + 2 * C[i])) / 3
    d[i] = (C[i + 1] - C[i]) / 3 / h[i]

print(a, b, c, d)

for i in range(1, n):
    print(a[i], b[i], c[i], d[i])

i = 0
j = 0

if j < n:
    j = j + 1

    if (xp >= x[j - 1]) and (xp <= x[j]):
        i = j
        j = n

if i == 0:
    print(xp)

else:
    Yp = a[i] + b[i] * (xp - x[i - 1]) + c[i] * pow((xp - x[i - 1]), 2) + d[i] * sqrt(xp - x[i - 1]) * (xp - x[i - 1])

print('f(xp)=', Yp)
