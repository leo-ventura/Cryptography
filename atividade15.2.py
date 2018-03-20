def inverso(a, mod):
    modfixo = mod
    x1 = 1
    x = 0
    y1 = 0
    y = 1
    #print a, '-', x1, y1
    #print mod, '-', x, y
    while a%mod > 0:
        r = a%mod
        q = a/mod
        if r != 0:
            #print r, q, '-', '-'
            #print r, q, x1-q*x, y1-q*y
            a = mod
            mod = r
            xr = x1
            x1 = x
            x = xr-q*x
            yr = y1
            y1 = y
            y = yr-q*y
    #print 0, a/mod, '-', '-'
    if r == 1:
        while x < 0:
            i = 1
            x = x + modfixo*i
            i = i + 1
        if x > modfixo:
            x = x%modfixo
    return x

def potenciamodular(a, e, mod):
    r = 1
    while e > 0:
        if e%2 == 1:
            #print r, a, e, 'S'
            r = (r*a)%mod
            e = (e-1)/2
        else:
            #print r, a, e, 'N'
            e = e/2
        a = (a*a)%mod
    return r

k = input()
for _ in range(k):
    g, h, p = input()
    m = int((p-1)**0.5) + 1
    print m
    j = 0
    gj = [] # lista com os valores de j
    while j < m:
        print j, (g**j)%p
        gj.append((g**j)%p)
        j = j + 1
    glinha = inverso(g, p) # calculo o inverso de g
    t = potenciamodular(glinha, m, p) # calculo t usando o RAE IMPAR (pego o ultimo valor)
    i = 0
    while (h*(t**i))%p not in gj: #faco o loop ate achar um valor de h*t^i (mod p) que esteja na lista dos valores de j
        print i, (h*(t**i))%p
        i = i+1
    print i, (h*(t**i))%p # como o loop acaba quando eu acho o valor, eu printo o valor de i que encontrou o valor e o tal valor
    print i, gj.index((h*(t**i))%p) # aqui printo i novamente e o valor em que h*t^i (mod p) se encontra na lista
    print i*m + gj.index((h*(t**i))%p) 
    print '---'
