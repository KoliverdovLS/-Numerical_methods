xi=int(input())

yi=int(input())

zi=int(input())

h=float(input())

N=int(input())

def f1(x,y,z):

    return -y-z

def f2(x,y,z):

    a=0.15

    return x+a*y

def f3(x,y,z,c):
    b = 0.2

    return b + z * (x - c)

def k0(h, xi, yi, zi):

    return h * f1(xi, yi, zi)

def l0(h, xi, yi, zi):

    return h * f2(xi, yi, zi)

def n0(h, xi, yi, zi, c):

    return h * f3(xi, yi, zi, c)

def k1(h, xi, yi, zi, k0, l0):

    return h * f1(xi + h / 2, yi + k0 / 2, zi + l0 / 2)

def l1(h, xi, yi, zi, k0, l0):

    return h * f2(xi + h / 2, yi + k0 / 2, zi + l0 / 2)

def n1(h, xi, yi, zi, k0, l0, c):

    return h * f3(xi + h / 2, yi + k0 / 2, zi + l0 / 2, c)

def k2(h, xi, yi, zi, k1, l1):

    return h * f1(xi + h / 2, yi + k1 / 2, zi + l1 / 2)

def l2(h, xi, yi, zi, k1, l1):

    return h * f2(xi + h / 2, yi + k1 / 2, zi + l1 / 2)

def n2(h, xi, yi, zi, k1, l1, c):

    return h * f3(xi + h / 2, yi + k1 / 2, zi + l1 / 2, c)

def k3(h,xi,yi,zi,k2,l2):

    return h*f1(xi+h,yi+k2,zi+l2)

def l3(h,xi,yi,zi,k2,l2):

    return h*f2(xi+h,yi+k2,zi+l2)

def n3(h,xi,yi,zi,k2,l2,c):

    return h*f3(xi+h,yi+k2,zi+l2,c)

c=3

Xi=xi

Yi=yi

Zi=zi

while c<10:

    print('Параметр с =',c,'\n')

    for i in range(0,N):

        print('x[',i,'] =',xi,'\t','y[',i,'] =',yi,'\t','z[',i,'] =',zi)

        K0=k0(h,xi,yi,zi)

        L0=l0(h,xi,yi,zi)

        N0=n0(h,xi,yi,zi,c)

        K1=k1(h,xi,yi,zi,K0,L0)

        L1=l1(h,xi,yi,zi,K0,L0)

        N1=n1(h,xi,yi,zi,K0,L0,c)

        K2=k2(h,xi,yi,zi,K1,L1)

        L2=l2(h,xi,yi,zi,K1,L1)

        N2=n2(h,xi,yi,zi,K1,L1,c)

        xi=xi+1/6*(K0+2*K1+2*K2+k3(h,xi,yi,zi,K2,L2))

        yi=yi+1/6*(L0+2*L1+2*L2+l3(h,xi,yi,zi,K2,L2))

        zi=zi+1/6*(N0+2*N1+2*N2+n3(h,xi,yi,zi,K2,L2,c))

    xi=Xi

    yi=Yi

    zi=Zi

    c=c+1

    print('\n')

