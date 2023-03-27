"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de inserir,
apagar e listar valores da sua lista.
Não permita que o programa quebre com erros
de indices inexistentes na lista.
"""

lista_de_compras = []

while True:
    menu = str(input('\n\nSelecione uma opção:\n'\
                    '[i]nserir [a]pagar [l]istar '))
    if menu in str('ialIAL'):
        pass
    else:
        print('\nValor IMPOSSÍVEL')
        continue
    if menu == 'i' or menu == 'I':
        lista_de_compras.append(input('Compra a ser adicionada: '))
    elif menu == 'a' or menu == 'A':
        if len(lista_de_compras) == 0:
            print('Nenhum valor adicioanado ainda.')
            continue
        indice_compra = input('Digite o valor que deseja remover: ')
        try:
            indice_compra = int(indice_compra)
        except:
            print('\nValor IMPOSSÍVEL')
            continue
        try:
            lista_de_compras.remove(lista_de_compras[indice_compra])
        except:
            print('\nValor fora do alcance')
    elif menu == 'l' or menu == 'L':
        if len(lista_de_compras) == 0:
            print('Nenhum valor adicioanado ainda.')
        else:
            print()
            for indice,compra in enumerate(lista_de_compras):
                print(indice,compra)
    else:
        print('!!!Algo deu errado!!!')