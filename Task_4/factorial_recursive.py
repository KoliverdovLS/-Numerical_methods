
def calc_factorial(n,sum=1):
    if n <= 1: return sum
    sum *= (n);
    return calc_factorial((n-1),sum)

print(calc_factorial(5));