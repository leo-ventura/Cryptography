n = input()
for _ in range(n):
    b, e, mod = input()
    temp = mod
    primos = []
    possivelD = 2
    while possivelD <= temp:
        if temp%possivelD == 0:
            expo = 0
            while temp%possivelD == 0:
                expo = expo + 1
                temp = temp/possivelD
            print possivelD, expo
            primos.append(possivelD)
        possivelD = possivelD + 1
    valores = []
    for k in primos:
	etmp = e
	base = b
        if e%(k-1) == 0:
            print 0
            valores.append((b**e)%k)
        else:
	    print e%(k-1)
            etmp = etmp%(k-1)
	    valores.append((b**etmp)%k)
            r = 1
            while etmp > 0:
                if etmp%2 == 1:
                    print r, base, etmp, 'S'
                    r = (r*base)%k
                    etmp = (etmp-1)/2
                else:
                    print r, base, etmp, 'N'
                    etmp = etmp/2
                base = (base*base)%k
            print r, base, 0, 'N'
    x1 = 1
    x = 0
    y1 = 0
    y = 1
    primeiro = primos[0]
    segundo = primos[1]
    print primeiro, '-', x1, y1
    print segundo, '-', x, y
    r = 1
    while r > 0:
        r = primeiro%segundo
        q = primeiro/segundo
        if r == 0:
            print r, q, '-', '-'
        else:
            print r, q, x1-q*x, y1-q*y
            primeiro = segundo
            segundo = r
            xr = x1
            x1 = x
            x = xr-q*x
            yr = y1
            y1 = y
            y = yr-q*y
    print x, y
    valor = (valores[0]*y*primos[1] + valores[1]*x*primos[0])%(primos[0]*primos[1])
    modulo = primos[0]*primos[1]
    print valor, modulo
    i = 1
    while i < len(valores)-1:
        x1 = 1
        x = 0
        y1 = 0
        y = 1
        primeiro = modulo
        segundo = primos[i + 1]
        print primeiro, '-', x1, y1
        print segundo, '-', x, y
        r = 1
        while r > 0:
            r = primeiro%segundo
            q = primeiro/segundo
            if r == 0:
                print r, q, '-', '-'
            else:
                print r, q, x1-q*x, y1-q*y
                primeiro = segundo
                segundo = r
                xr = x1
                x1 = x
                x = xr-q*x
                yr = y1
                y1 = y
                y = yr-q*y
        print x, y
        valor = (valor*y*primos[i + 1] + valores[i+1]*x*modulo)%(modulo*primos[i + 1])
        modulo = modulo*primos[i + 1]
        print valor, modulo
        i = i + 1
    print '---'
