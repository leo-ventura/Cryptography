def atividade62(a, e, mod):
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
    print '---'

m = input()
for _ in range(m):
    k = input()
    fermat = 2**2**k + 1
    print fermat
    atividade62(5, (fermat-1)/2, fermat)
