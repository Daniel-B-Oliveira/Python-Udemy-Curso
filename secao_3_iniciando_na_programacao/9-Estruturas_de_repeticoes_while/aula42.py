frase = 'Python é uma linguagem de programação'\
        ', multiparadigma, '\
        'que foi criada por Guido van Rossum.'

i = 0

qtd_apareceu_mais_vezes = 0

letra_apareceu_maiz_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_vezes_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_vezes_atual
        letra_apareceu_maiz_vezes = letra_atual


    i += 1

print(f'A letra que apareceu mais vezes foi \'{letra_apareceu_maiz_vezes}\''
      f' {qtd_apareceu_mais_vezes}X')

