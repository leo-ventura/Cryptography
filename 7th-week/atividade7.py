# algoritmo para encontrar os inversos multiplicativos
# baseado no Euclidiano Estendido

n = input()
for e in range(n):
    a, mod = input()
    modfixo = mod
    x1 = 1
    x = 0
    y1 = 0
    y = 1
    print a, '-', x1, y1
    print mod, '-', x, y
    while a%mod > 0:
        r = a%mod
        q = a/mod
        if r == 0:
            print r, q, '-', '-'
        else:
            print r, q, x1-q*x, y1-q*y
            a = mod
            mod = r
            xr = x1
            x1 = x
            x = xr-q*x
            yr = y1
            y1 = y
            y = yr-q*y
    print 0, a/mod, '-', '-'
    if r == 1:
        while x < 0:
            i = 1
            x = x + modfixo*i
            i = i + 1
        if x > modfixo:
            x = x%modfixo
        print x
    else:
        print 0
    print '---'
