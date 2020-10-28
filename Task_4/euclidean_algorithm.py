def NOD (a, b):
    if a == b: return a
    if a > b:
        a = a - b
    else:
        b = b - a

    print(a,'--',b)
    return NOD(a,b)

print(NOD(140,56))
