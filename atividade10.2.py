# Programa para calcular a funcao Fi

k = input()
for _ in range(k):
    a = input()
    n = a
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
    print '---'
