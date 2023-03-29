import os

# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load


caminho_arquivo=\
r'C:\\Users\\danie\\Documents\\curso_python\\udemy_python\\secao_4_python_intermediario\\10-final_secao_4\\aula116.txt'

print(caminho_arquivo)
# arquivo = open(caminho_arquivo, 'w')

# arquivo.close()

# with open(caminho_arquivo, 'w+') as arquivo:
#     arquivo.write('Teste 123\n')
#     arquivo.write('Teste 123\n')
#     arquivo.writelines(
#         ('Linha 3\n', 'Linha 4\n')
#     )
#     arquivo.seek(0, 0)
#     print(arquivo.read())
#     print('lendo')
#     arquivo.seek(0, 0)
#     print(arquivo.readline(), end='')
#     print('Arquivo vai ser fechado')

# with open(caminho_arquivo, 'r') as arquivo:
#     print(arquivo.read())

with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
    arquivo.write('Teste 123\n')
    arquivo.write('Teste 123 Ç Ç Ç \n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )

# os.unlink(caminho_arquivo)

# os.rename(caminho_arquivo, 'arla116-2.txt')