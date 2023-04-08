# Usando subprocess para executar e comandos externos
# subprocess é um módulo do Python para executar
# processos e comandos externos no seu programa.
# O método mais simples para atingir o objetivo é usando subprocess.run().
# Argumentos principais de subprocess.run():
# - stdout, stdin e stderr -> Redirecionam saída, entrada e erros
# - capture_output -> captura a saída e erro para uso posterior
# - text -> Se True, entradas e saídas serão tratadas como texto
# e automaticamente codificadas ou decodificadas com o conjunto
# de caracteres padrão da plataforma (geralmente UTF-8).
# - shell -> Se True, terá acesso ao shell do sistema. Ao usar
# shell (True), recomendo enviar o comando e os argumentos juntos.
# - executable -> pode ser usado para especificar o caminho
# do executável que iniciará o subprocesso.
# Retorno:
# stdout, stderr, returncode e args
# Importante: a codificação de caracteres do Windows pode ser
# diferente. Tente usar cp1252, cp852, cp850 (ou outros). USEI0> cp852
#Linux e mac, use utf_8.
# Comando de exemplo:
# Windows: ping 127.0.0.1
# Linux/Mac: ping 127.0.0.1 -c 4

import subprocess
import sys
from pathlib import Path


CAMINHO_CHAVE = 'C:\\Users\\danie\\Documents\\curso_python\\udemy_python\\secao_6_modulos_python\\10-Subprocess\\Teste.pem'
print(CAMINHO_CHAVE)
cmd = ['ping','127.0.0.1', '-c', '4']
encondig = 'UTF-8'

system = sys.platform

if system == 'win32':
    cmd = [f'ssh -i C:\\Users\\danie\\Documents\\curso_python\\udemy_python\\secao_6_modulos_python\\10-Subprocess\\Teste.pem ubuntu@44.212.21.106',]
    encondig = 'cp852'

# ssh -i C:\\Users\\danie\\Documents\\curso_python\\udemy_python\\secao_6_modulos_python\\10-Subprocess\\Teste.pem ubuntu@44.212.21.106

proc = subprocess.run(
    cmd,
    capture_output=True,
    text=True,
    encoding=encondig
    # shell=True 
)

# print()
# print(proc.args)
# print(proc.stderr)
# print(proc.returncode)
# print(proc.stdout.decode('cp852')) if text = False
print(proc.stdout)
