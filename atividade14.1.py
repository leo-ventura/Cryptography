k = input()
for _ in range(k):
    p = input()
    pfixo = p
    mersene = 2**p - 1
    print mersene
    rmax = ((2**p)**0.5 - 1)/(2.0*p)
    if int(rmax) == rmax:
        rmax = rmax-1
    else:
        rmax = int(rmax)
    erre = 1
    print rmax
    achou = 0
    while erre <= rmax:
        print erre
        p = pfixo
        a = 2
        q = 1 + 2*erre*p
        r = 1
        while p > 0:
            if p%2 == 1:
                print r, a, p, 'S'
                r = (r*a)%q
                p = (p-1)/2
            else:
                print r, a, p, 'N'
                p = p/2
            a = (a*a)%q
        print r, a, 0, 'N'
        if r == 1:
            print q
            achou = 1
            break
        else:
            erre = erre + 1
    if achou == 0:
        print mersene
    print '---'