# algoritmo da potenciacao modular (R/A/E/IMPAR?)

n = input()
for e in range(n):
    a, e, mod = input()
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
