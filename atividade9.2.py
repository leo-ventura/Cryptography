n = input()
for _ in range(n):
    a, b = input()
    x1 = 1
    x = 0
    y1 = 0
    y = 1
    primeiro = b[0]
    segundo = b[1]
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
    valor = (a[0]*y*b[1] + a[1]*x*b[0])%(b[0]*b[1])
    modulo = b[0]*b[1]
    print valor, modulo
    i = 1
    while i < len(a)-1:
        x1 = 1
        x = 0
        y1 = 0
        y = 1
        primeiro = modulo
        segundo = b[i + 1]
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
        valor = (valor*y*b[i + 1] + a[i + 1]*x*modulo)%(modulo*b[i + 1])
        modulo = modulo*b[i + 1]
        print valor, modulo
        i = i + 1
    print '---'
