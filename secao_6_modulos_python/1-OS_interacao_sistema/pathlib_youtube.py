# https://youtu.be/T17BTNKBeJY

from pathlib import Path

# caminho_projeto = Path()
# print(caminho_projeto.absolute())
# print(caminho_arquivo)
# ideias = caminho_arquivo.parent / 'ideias'
# print(ideias / 'arquivo.txt')
# arquivo = Path.home() / 'Desktop' / 'arquivo.txt'


# with caminho_arquivo.open('a+') as file:
#     file.write('Uma linha\n')
#     file.write('Outra linha 123\n')

# caminho_arquivo = Path.home() / 'Desktop' / 'arquivo_aula_youtube.txt'
# caminho_arquivo.touch()
# caminho_arquivo.write_text('Olá, Mundo!')
# caminho_arquivo.unlink()

caminho_pasta = Path.home() / 'Desktop' / 'Teste Python !!! ~^ É'

caminho_pasta.mkdir(exist_ok=True)

arquivo = caminho_pasta / 'Teste.txt'
arquivo.touch()
arquivo.write_text('TESTE TESTE 123')


