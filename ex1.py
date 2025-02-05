def reverter_caracteres(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverter_caracteres(s[:-1])
    
string = "diogo"
print(f'A string invertida fica: {reverter_caracteres(string)}')