def square(s1):
    for i in range(1, s1 + 1):
        for j in range(i, i * s1 + 1, i):
            print(j, end='\t')
        print()

square(10);