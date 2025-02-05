def indice_maior_elemento(lista, indice = 0, maior = 0): 
    if indice == len(lista):
        return maior
    if lista[indice]>lista[maior]:
        maior = indice
    return indice_maior_elemento(lista, indice + 1, maior)


lista_num = ([1, 5, 3, 9, 2])
print(f'O maior número está no índice: {indice_maior_elemento(lista_num)}')