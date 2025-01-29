# Exercício 3: Contar Caracteres em uma String
# Crie uma função recursiva chamada contar_caracteres(s, c) que conta quantas vezes o
# caractere c aparece na string s.
# Exemplo de Entrada:
# contar_caracteres("banana", "a")
# Saída Esperada:
# 3

def contar_caracteres(s,c):
    if not s:
        return 0
    else:
        return (1 if s[0] == c else 0) + contar_caracteres(s[1:], c)
    
print(contar_caracteres('banana', 'a'))