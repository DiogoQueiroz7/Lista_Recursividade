def contar_caracteres(s,c):
    if not s:
        return 0
    else:
        return (1 if s[0] == c else 0) + contar_caracteres(s[1:], c)

print(f'A quantidade dos caracteres na palavra é: {contar_caracteres("banana", "a")}')
