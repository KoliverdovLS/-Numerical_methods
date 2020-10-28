def two_numercial (a,b):
    if a == b: return "Enter different numbers"
    if a > b:
        a = 2*a * b
        b = ((a / 2 / b) + b) / 2
    else:
        b = 2*a * b
        a = (a + (b / 2 / a)) / 2

    return a,b

print(two_numercial(5,6))
