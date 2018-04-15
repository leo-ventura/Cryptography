k = input()
for _ in range(k):
    nrsa, ersa, bloco = input()
    a = nrsa
    x = int(nrsa**0.5)
    y = 0
    resposta = ''
    while resposta != 'S':
        if a != x**2 - y**2:
            resposta = 'N'
        print x, y, resposta
        x = x + 1
        y = int((x**2-a)**0.5)
        if x == (a+1)/2:
            print 1, a
            break
        if a == x**2 - y**2:
            resposta = 'S'
            print x, y, resposta
            break
    if x != (a+1)/2:
        print x-y, x+y
    a = nrsa
    n = nrsa
    if a >=2:
        possivelD = 2
        while possivelD <= a:
            if a%possivelD == 0:
                e = 0
                while a%possivelD == 0:
                    e = e + 1
                    a = a/possivelD
            possivelD = possivelD + 1
    U = [1] #lista com os valores que U(n) vai receber
    i = 1
    divisores = []
    while i < n:
        if n%i == 0:
            divisores.append(i)
        i = i + 1
    i = 1
    while i < len(divisores):
        j = 2
        while divisores[i] * j < n:
            e = divisores[i] * j
            divisores.append(e)
            j = j + 1
        i = i + 1
    i = 1
    while i < n:
        if n%i != 0 and i not in divisores:
            U.append(i)
        i = i + 1
    print len(U)
    b = len(U)
    a = ersa
    x1 = 1
    x = 0
    y1 = 0
    y = 1
    print a, '-', x1, y1
    print b, '-', x, y
    r = 1
    while r > 0:
        r = a%b
        q = a/b
        if r == 0:
            print r, q, '-', '-'
        else:
            print r, q, x1-q*x, y1-q*y
            a = b
            b = r
            xr = x1
            x1 = x
            x = xr-q*x
            yr = y1
            y1 = y
            y = yr-q*y
    if x < 0:
        d = x+len(U)
    else:
        d = x%len(U)
    print d
    e = d
    a = bloco
    r = 1
    mod = nrsa
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
    print r
    print '---'