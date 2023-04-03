# os + shutil - Apagando, copiando, movendo e renomeando pastas com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
# Copiar Árvore recursivamente -> shutil.copytree
# Apagar Árvore recursivamente -> shutil.rmtree
# Apagar arquivos -> os.unlink
# Renomear/Mover -> shutil.move ou os.rename

import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'secao_3_iniciando_na_programacao')
NOVA_PASTA = os.path.join(DESKTOP, 'copia')

print(DESKTOP)

# shutil.rmtree(NOVA_PASTA)
# shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)
