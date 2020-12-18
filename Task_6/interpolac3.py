Xp=float(input())

n=int(input())

X=[]

Y=[]

for i in range(0,n):

    X.append(float(input()))

    Y.append(float(input()))

if Xp<X[0]:

    print('экстраполяция назад')

    i=1

elif Xp>X[n-1]:

    print('экстраполяция вперед')

    i=n

else:

    j=0

    while j<n:

        j=j+1

        if Xp>=X[j-1] and Xp<=X[j]:

            i=j

            j=n

A=(Y[i]-Y[i-1])/(X[i]-X[i-1])

B=Y[i-1]-A*X[i-1]

Yp=A*Xp+B

print('Xp =',Xp)

print('X =',X)

print('Y =',Y)

print('f(Xp) =',Yp)