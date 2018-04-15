n = input()
for _ in range(n):
    a, base = input()
    b = base
    e = 0
    k = a - 1
    while k%2 == 0:
        e = e + 1
        k = k/2
    print e, k
    r = 1
    temp = k
    while temp > 0:
        if temp%2 == 1:
            print r, base, temp, 'S'
            r = (r*base)%a
            temp = (temp-1)/2
        else:
            print r, base, temp, 'N'
            temp = temp/2
        base = (base*base)%a
    print r, base, 0, 'N'
    t = (b**k)%a
    print k, t
    if t == 1 or t == a-1:
        print 2*k, t
        print 'INCONCLUSIVO'
    else:
        i = 1
        ja = 1
        while i < e:
            k = k*2%a
            t = (t*t)%a
            if t == a-1:
                print k, t
                print 'INCONCLUSIVO'
                ja = 0
                break
            i = i + 1
            print k, t
        if ja:
            print 'COMPOSTO'
    print '---'
