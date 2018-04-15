def mdc(a, b):
    while a%b > 0:
        r = a%b
        a = b
        b = r
    return r

k = input()
for _ in range(k):
    n = input()
    U = []
    for e in range(1, n):
        if mdc(e, n) == 1:
            U.append(e)
    print U
    print [1]
    i = 1
    while i < len(U):
        cic = [1]
        k = 1
        while (U[i]**k)%n != 1:
            cic.append((U[i]**k)%n)
            k = k + 1
        print sorted(cic)
        i = i + 1
    print '---'
