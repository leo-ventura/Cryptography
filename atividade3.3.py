n = input()
for _ in range(n):
    a = input()
    x = int(a**0.5)
    y = 0
    if a%2 != 0:
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
    print '---'
