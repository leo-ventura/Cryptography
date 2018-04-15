n = input()
for e in range(n):
    a, b = input()
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
    print '---'
