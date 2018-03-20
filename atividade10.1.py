# Programa calcula os valores de U(n) dado n

k = input()
for _ in range(k):
    n = input() #entra com o valor n
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
    print U
