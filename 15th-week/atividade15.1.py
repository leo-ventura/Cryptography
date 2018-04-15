def potenciamodular(a, e, mod):
    r = 1
    while e > 0:
        if e%2 == 1:
            print r, a, e, 'S'
            r = (r*a)%mod
            e = (e-1)/2
        else:
            print r, a, e, 'N'
            e = e/2
        a = (a*a)%mod
    print r, a, 0, 'N'
    return r

k = input()
for _ in range(k):
    p, a, s, t = input()
    slinha = potenciamodular(s, p-1-a, p)
    print (slinha*t)%p
    print '---'
