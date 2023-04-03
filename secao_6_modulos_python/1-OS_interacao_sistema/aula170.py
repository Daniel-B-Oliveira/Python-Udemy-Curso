# os.listdir para navegar em caminhos
import os

# caminho = 'C:\\Users\\danie\\Documents\\curso_python\\udemy_python\\secao_6_modulos_python\\1-OS_interacao_sistema'

caminho = os.path.join('C:\\',
                       'Users',
                       'danie',
                       'Documents',
                       'curso_python',
                       'udemy_python',
                       'secao_6_modulos_python',
                       '1-OS_interacao_sistema',
                       )

print(caminho)

# Usado para verificar os itens na pasta

# for pasta in os.listdir(caminho):
#     caminho_completo_pasta = os.path.join(caminho, pasta)
#     # print(pasta)
#     print(caminho_completo_pasta)