n = input()
if n >= 3:
    todos = []
    atual = 3
    while atual <= n:
        todos.append(atual)
        atual = atual + 2
    print todos
    print int(n**0.5)
    atual = 3
    cortados_geral = []
    mantidos = todos
    while atual <= n**0.5 and atual not in cortados_geral:
        inicio = atual*atual
        pos = int((atual*atual-3)/2)
        print atual, inicio, pos
        mantidos = []
        cortados = []
        while pos <= len(todos)-1:
            adicionado = todos[pos]
            cortados.append(adicionado)
            pos = pos + atual
            if adicionado not in cortados_geral:
                cortados_geral.append(adicionado)
        for e in todos:
            if e not in cortados_geral:
                mantidos.append(e)
        print cortados
        print mantidos
        atual = atual + 2
    print [2] + mantidos
