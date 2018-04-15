# Teorema de Fermat que informa que, se mdc = 1 é inconclusivo e se for != de 1
# eh composto

n = input()
for elements in range(n):
    e, a = input()
    efixo = e
    e = e-1
    r = 1
    while e > 0:
        if e%2 == 1:
            print r, a, e, 'S'
            r = (r*a)%efixo
            e = (e-1)/2
        else:
            print r, a, e, 'N'
            e = e/2
        a = (a*a)%efixo
    print r, a, 0, 'N'
    if r == 1:
        print 'INCONCLUSIVO'
    else:
        print 'COMPOSTO'
    print '---'
