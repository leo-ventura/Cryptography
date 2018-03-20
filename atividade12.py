def mdc(a, b):
    while a%b > 0:
        r = a%b
        a = b
        b = r
    return r

k = input()
for _ in range(k):
    p = input()
    possivelD = 2
    pfixo = p
    p = p - 1
    fatores = []
    expoentes = []
    while possivelD <= p:
        if p%possivelD == 0:
            e = 0
            while p%possivelD == 0:
                e = e + 1
                p = p/possivelD
            fatores.append(possivelD)
            expoentes.append(e)
            print possivelD, e
        possivelD = possivelD + 1
    g = 1
    i = 0
    while i < len(fatores):
        a = 2
        while a**((pfixo-1)/fatores[i])%pfixo == 1:
            a = a + 1
        h = a**((pfixo-1)/(fatores[i]**expoentes[i]))%pfixo
        g = (g*h)%pfixo
        print fatores[i], a, h
        i = i+1
    print g
    listag = []
    i = 1
    while i < pfixo-1:
        if mdc(i, pfixo-1) == 1:
            listag.append(int(g**i%pfixo))
        i = i+1
    print sorted(listag)
