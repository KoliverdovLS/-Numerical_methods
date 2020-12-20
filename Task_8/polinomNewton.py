N = int(input())
X = []
Y = []

for i in range(0, N + 1):
    X.append(int(input()))
    Y.append(int(input()))

D = [0 for n in range(1, N + 1) for nn in range(2, N + 1)]

for j in range(1, N + 1):
    D[j][1] = Y[j] - Y[j - 1]

for j in range(2, N + 1):
    for i in range(1, N + 1):
        D[i][j] = 0

for j in range(2, N + 1):
    for i in range(1, N - J + 2):
        D[i][j] = D[i + 1, j - 1] - D[i, j - 1]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        print('D[', i, ',', j, '] =', D[i][j])

C = int(input())
P1 = 2
Z = N

for i in range(0, N):

    if C < X[i]:
        P1 = 2
        Z = N

    elif C <= X[i + 1]:

        if i <= N % 2:
            P1 = 1
            Z = i

        else:
            P1 = 2
            Z = i + 1

U = 1
P = 1
H = X[1] - X[0]
t = (C - X[Z]) / H
Y0 = Y[Z]

if P1 == 1:

    for i in range(1, N - Z):
        P = P * i
        U = U * (t - i + 1)
        Y0 = Y0 + U * D[Z + 1][i] / P

else:
    K = 0

    for i in range(Z, 2):
        K = K + 1
        P = P * K
        U = U * (t + K - 1)
        Y0 = Y0 + U * D[i - 1][K] / P

print('C =', C, '\tY0 =', Y0)
