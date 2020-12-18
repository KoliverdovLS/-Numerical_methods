def education(x):
    y = -2.4*(x ** 2) + 5*x - 3
    return round(y, 3)

print('x1->')
x1=float(input())
print('x2->')
x2=float(input())
print('dx->')
dx=float(input())
print('---------------')
print('x    |     y')
print('---------------')

while x1<=x2:
    print(x1,' |   ', education(x1))
    x1 = x1 + dx