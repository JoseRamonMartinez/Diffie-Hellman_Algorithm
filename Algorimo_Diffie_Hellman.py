
def algoritmo_Diffie_Hellman():
    '''Código del algoritmo de intercambio de clave con parametros p, x y n ya establecidos.'''
    p=98456837582149837574896713876468943674631573897892782758947597489573486973489578493768748967438957489375893476897468947368948363
    x=747563477345748573453464234235235234234234235235234234234353534534534534456431231456412131231345764131231464132124345645612314413
    n=923145873568473895341058230498058304975094381694385094839869348609438189547509438509438610983049860934860934860934863487534897877

    z = ExpMod(n,x,p)
    print('La clave z publica es :\n',z)
    print('\nIntroduce la z del otro usuario:')
    z_2 = input()
    t = ExpMod(z_2,x,p)
    print('La clave z privada es para los dos usuarios es: ',t, '\nPor favor, solo enviala por un medio seguro')
    input()


def ExpMod(a,n,z):
    '''Funcion exponencial usada por el algoritmo'''
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

def ataque_fuerza_bruta():
    '''Codigo para la realización de ataque por fuerza bruta con parametros ya establecidos'''
    n=253
    p=131074
    z1=79525
    z2=106243
    x1=0
    x2=0
    t1=666
    t2=666

    while(t1!=z1):
        t1 = ExpMod(n,x1,p)
        x1+=1

    while(t2!=z2):
        t2 = ExpMod(n,x2,p)
        x2+=1

    print("Valor x1=",x1-1,", valor x2=",x2-1,"\n")
    x3=(x1-1)*(x2-1)
    z_privada = ExpMod(n,x3,p)
    print("La clave privada es",z_privada)
    input()


def seleccion():
    '''Selector de funcion del programa'''
    print("Introduce '1' para acceder al algoritmo o '2'  para acceder al ataque por fuerza bruta")
    s=input()
    if(s=='1'):
        algoritmo_Diffie_Hellman()
    else:
        ataque_fuerza_bruta()


seleccion()

