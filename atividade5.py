k = input()
maior = 1 #quantidade de divisores do numero com mais divisores
testehcn = 2 #numero atual
hcn = [1] #lista com todos os hcn menores que k
while testehcn <= k: #fazer loop ate chegar a k
    fator = 1 #fatores para dividir
    lista = [] #lista com os divisores do numero atual
    while testehcn >= fator:
        if testehcn % fator == 0:
            lista.append(fator)
        fator = fator + 1
    if len(lista) > maior:
        maior = len(lista)
        hcn.append(testehcn)
    testehcn = testehcn + 2
print hcn
