xi = int(input())

xxi = int(input())

a = int(input())

h = float(input())

N = int(input())


def f1(x, xx, a):
    return (a - x * x) * xx - x


def k0(h, xi, xxi, a):
    return h * f1(xi, xxi, a)


def k1(h, xi, xxi, k0, a):
    return h * f1(xi + h / 2, xxi + k0 / 2, a)


def k2(h, xi, xxi, k1, a):
    return h * f1(xi + h / 2, xxi + k1 / 2, a)


def k3(h, xi, xxi, k2, a):
    return h * f1(xi + h, xxi + k2, a)


for i in range(0, N):
    print('x[', i, '] =', xi)

    K0 = k0(h, xi, xxi, a)

    K1 = k1(h, xi, xxi, K0, a)

    K2 = k2(h, xi, xxi, K1, a)

    xi = xi + 1 / 6 * (K0 + 2 * K1 + 2 * K2 + k3(h, xi, xxi, K2, a))

print('\n')
