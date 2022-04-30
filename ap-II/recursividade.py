def somaListaRec(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + somaListaRec(lista[1:])


listinha = [1,2,3,4,5]
print(somaListaRec(listinha))
