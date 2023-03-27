"""
split e join com list e str
split - divide uma string
join - une uma sring

strip, lstrip, rstrip = remove os espaços nas extremidades, apenas esquerda, apenas direita


"""

frase = '    Olha só que   ,   coisa interessante   '
lista_frases_originais = frase.split(', ')

lista_frases = []

for i, frase in enumerate(lista_frases_originais):
    lista_frases.append(lista_frases_originais[i].strip())


# print(lista_frases)

frases_unidas = ', '.join(lista_frases)
print(frases_unidas)
