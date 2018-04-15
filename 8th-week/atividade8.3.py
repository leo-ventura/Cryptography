n = input()
for _ in range(n):
    a = input()
    afixo = a
    if a >=2:
        possivelD = 2
        while possivelD <= a:
            if a%possivelD == 0:
                e = 0
                while a%possivelD == 0:
                    e = e + 1
                    a = a/possivelD
                print possivelD, e
                if possivelD == afixo:
                    carmichael = 'NAO'
                elif afixo%(possivelD-1) == 1 and e == 1:
                    carmichael = 'SIM'
                else:
                    carmichael = 'NAO'
            possivelD = possivelD + 1
    print carmichael
    print '---'
