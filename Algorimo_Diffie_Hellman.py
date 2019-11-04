def algoritmo_Diffie_Hellman():
    #z = n^x mod p
    p=761
    x=10
    n=9857
    z = ExpMod(n,x,p)
    print(z)
    z = (Elevar(n,x) % p)
    print (z)

def Elevar(n,x):
    numero=n
    for i in range(1, x):
        numero=numero*n
    return numero

def ExpMod(a,n,z):
    if (n == 0):
        return 1
    else:
        if ((n & 1) == 0):
            r=ExpMod(a,n-1,z)
            return ((a*r) % z)
        else:
            r=ExpMod(a,n/2,z)
            return ((r*r) % r)


algoritmo_Diffie_Hellman()
