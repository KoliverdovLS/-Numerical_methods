# Задача аналогичная заданию со второй недели

def calculate_factorial(n):
    if n < 0:
        return 'error'

    if n == 0:
        return 1

    result = 1
    i = 1
    while i < n:
        result += result * i
        i += 1
    return result

def function(x,n):
    i = 0
    result = 0
    while i <= n:
        result += (x ** i)/calculate_factorial(i)
        i += 1

    return result

print(function(1,2))