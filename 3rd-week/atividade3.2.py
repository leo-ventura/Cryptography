n = input()
for _ in range(n):
    a = input()
    if a >=2:
        possivelD = 2
        while possivelD <= a:
            if a%possivelD == 0:
                e = 0
                while a%possivelD == 0:
                    e = e + 1
                    a = a/possivelD
                print possivelD, e
            possivelD = possivelD + 1
    print '---'
