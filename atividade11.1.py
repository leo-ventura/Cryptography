def mdc(h, n):
    while h%n > 0:
        r = h%n
        h = n
        n = r
    return r

k = input()
for _ in range(k):
    n, sub = input()
    U = []
    for i in range(1, n):
        if mdc(i, n) == 1:
            U.append(i)
    g = True
    for element in sub:
        if element in U:
            i = 0
            j = 0
            while i < len(sub)-1:
                if (sub[i] * sub[i+1])%n not in sub:
                    g = False
                i = i + 1
            if 1 not in sub:
                g = False
            for h in sub:
                if mdc(h, n) != 1:
                    g = False
        else:
            g = False
    if len(U)%len(sub) != 0:
        g = False
    if g:
        print 'SIM'
    else:
        print 'NAO'
