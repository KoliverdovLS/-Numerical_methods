def education(x):
    y = 2 * (x ** 2) - 5 * x - 8
    return y


x0 = -4
x = x0
print('|---------------|')
while x <= 4:
    y = education(x)
    print('  X: %i | Y: %i' % (x, y))
    x += 0.5
print('|---------------|')
