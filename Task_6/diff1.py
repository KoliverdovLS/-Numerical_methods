x0=int(input())

xk=int(input())

h=float(input())

N=3

Y0=[]

for i in range(0,N):

    y0=float(input())

    Y0.append(y0)

    print('Y0[',i,'] =',Y0[i])

def func(i,x0,Y0):

    if i==0:

        return 3*x0+Y0[0]-Y0[2]

    if i==1:

        return x0-Y0[1]+Y0[2]

    if i==2:

        return 5*x0-Y0[0]-Y0[1]

Y=[]

while x0<=xk:

    for i in range(0,N):

        Y.append(func(i,x0,Y0))

        print('X0 =',x0)

    x0=x0+h

    print('\n')

    for i in range(0,N):

        Y0[i]=Y0[i]+h*Y[i]

        print('Y0[',i,'] =',Y0[i])
