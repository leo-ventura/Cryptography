# algoritmo para calcular a potenciacao modular auxiliado pelo
# Teorema de Fermat

n = input()
for _ in range(n):
    a, e, mod = input()
    e = e%(mod-1) #unica parte que muda dele pro 6.2
    print e
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
