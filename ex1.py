#Exercício 1: Reverter os Caracteres de uma String
#Escreva uma função recursiva chamada reverter_caracteres(s) que recebe uma
#string s e devolve a string invertida. Não use laços (for ou while).

def reverter_caracteres(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverter_caracteres(s[:-1])
    
    
string = "diogo"
print(reverter_caracteres(string))