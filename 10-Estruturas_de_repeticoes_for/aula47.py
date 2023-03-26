"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

palavra_secreta = 'perfume'
palavra_formatada = '*' * len(palavra_secreta)
palavra_temporaria = ''
pontos = 1  # Não conta se o usário digitar mais de uma letra

while True:
    letra_input = input('Digite uma letra: ')
    if len(letra_input) != 1:
        print(palavra_formatada)
        continue
    if letra_input in palavra_secreta:
        for posicao in range(0, len(palavra_secreta)):
            if palavra_secreta[posicao] == letra_input:
                palavra_temporaria += letra_input
            else:
                palavra_temporaria += palavra_formatada[posicao]  # coloca o '*' ou a letra ja acertada naquela posi.
        palavra_formatada = palavra_temporaria[-len(palavra_secreta):]
    print(palavra_formatada)
    if palavra_formatada == palavra_secreta:
        break
    else:
        pontos += 1

print(f'\nVocê acertou a palavra \'{palavra_secreta}\', em {pontos} tentativas')
