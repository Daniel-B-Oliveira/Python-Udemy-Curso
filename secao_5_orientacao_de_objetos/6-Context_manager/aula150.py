# Context Maneger com funçaõ - Criando e Usando gerenciadores de contexto

# from contextlib import contextmanager

# @contextmanager
# def my_open(file_path, mode):
#     try:
#         file = open(file_path, mode, encoding='utf8')
#         yield file
#     except Exception as e:
#         print('Ocorreu erro', e)
#     finally:
#         file.close()

# PATH = 'C:\\Users\\danie\\Documents\\curso_python\\udemy_python\\secao_5_orientacao_de_objetos\\6-dunder\\'
# my_file_path = PATH + 'aula150.txt'

# with my_open(my_file_path, 'w') as file:
#     file.write('Linha 1\n')
#     file.write('Linha 2\n')
#     file.write('Linha 3\n')
#     print('WITH', file)


#       /           /           /           /           /


# from contextlib import contextmanager


# @contextmanager
# def my_open(caminho_arquivo, modo):
#     try:
#         print('Abrindo arquivo')
#         arquivo = open(caminho_arquivo, modo, encoding='utf8')
#         yield arquivo
#     except Exception as e:
#         print('Ocorreu erro', e)
#     finally:
#         print('Fechando arquivo')
#         arquivo.close()


# with my_open('aula150.txt', 'w') as arquivo:
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n', 123)
#     arquivo.write('Linha 3\n')
#     print('WITH', arquivo)