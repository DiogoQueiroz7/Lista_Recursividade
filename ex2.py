def soma_lista_aninhada(lista):
    soma = 0
    for i in lista:
        if isinstance(i,list):
            soma += soma_lista_aninhada(i)
        else:
            soma += i
    return soma

lista_num = ([1, [2, 3], [4, [5]]])

print(f'A soma da lista aninhada é: {soma_lista_aninhada(lista_num)}')
        
        
        