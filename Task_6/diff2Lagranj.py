N=int(input())

X=[]

Y=[]

for i in range(0,N):

    X.append(float(input()))

    Y.append(float(input()))

print('X =',X)

print('Y =',Y)

Xp=float(input())

print('Xp =',Xp)

Yp=0

for i in range(0,N):

    P=1

    for k in range(0,N):

        if i!=k:

            P=P*(Xp-X[k])/(X[i]-X[k])

    Yp=Yp+P*Y[i]

print ('Yp =',Yp)