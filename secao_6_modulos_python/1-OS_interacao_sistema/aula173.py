# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
# Apagar -> os.unlink
# Apagar -> diretorios recursivamente -> shutil.rmtree

import os
import shutil

HOME = os.path.expanduser('~')

DESKTOP = os.path.join(HOME, 'Desktop')

PASTA_ORIGINAL = os.path.join(DESKTOP, 'secao_3_iniciando_na_programacao')
NOVA_PASTA = os.path.join(DESKTOP, 'copia')

os.makedirs(NOVA_PASTA, exist_ok=True)

for root, dirs, files in os.walk(PASTA_ORIGINAL):
    # print(root)
    if root == 'C:\\Users\\danie\\Desktop\\secao_3_iniciando_na_programacao\\0-Introdução':
        print('TESTE')
    for dir_ in dirs:
        caminho_novo_diretorio = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_
            )
        
        print(caminho_novo_diretorio)
        os.makedirs(caminho_novo_diretorio, exist_ok=True)

    for file in files:
        caminho_arquivo = os.path.join(root, file) 
        caminho_novo_diretorio = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), file
            )
        
        shutil.copy(caminho_arquivo, caminho_novo_diretorio)

        print(caminho_arquivo)
