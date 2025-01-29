#Exercício 2: Soma de Números em uma Lista Aninhada
#Implemente uma função recursiva chamada soma_lista_aninhada(lista) que calcula a
#soma de todos os números em uma lista, mesmo que os números estejam dentro de
#sublistas (listas aninhadas).
#Exemplo de Entrada:
#soma_lista_aninhada([1, [2, 3], [4, [5]]])
#Saída Esperada:
#15 # (1 + 2 + 3 + 4 + 5)

def soma_lista_aninhada(lista):
    soma = 0
    for i in lista:
        if isinstance(i,list):
            soma += soma_lista_aninhada(i)
        else:
            soma += i
    return soma

    
    
lista = ([1, [2, 3], [4, [5]]])

print(soma_lista_aninhada(lista))