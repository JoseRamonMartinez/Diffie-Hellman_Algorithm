

def algoritmo_Diffie_Hellman():

    p=98456837582149837574896713876468943674631573897892782758947597489573486973489578493768748967438957489375893476897468947368948363
    x=47563477345748573453464234235235234234234235235234234234353534534534534
    n=23145873568473895341058230498058304975094381694385094839869348609438189547509438509438610983049860934860934860934863487534897877

    z = ExpMod(n,x,p)
    print('La clave z publica es :\n',z)
    print('\nIntroduce la z del otro usuario:')
    z_2 = input()
    t = ExpMod(z_2,x,p)
    print('La clave z privada es para los dos usuarios es: ',t, '\nPor favor, solo enviala por un medio seguro')
    input()







def ExpMod(a,n,z):
    a=int(a)
    n=int(n)
    z=int(z)
    r=1
    r=int(r)
    if (n == 0):
        return 1
    else:
        if (n%2!=0):
            r=ExpMod(a,n-1,z)
            return ((a*r) % z)
        else:
            r=ExpMod(a,n/2,z)
            return ((r*r) % z)


algoritmo_Diffie_Hellman()