from copy import deepcopy
import json

def executar_funcao(funcao):
    def interna(*args, **kwargs):
        try:
            return funcao(*args, **kwargs)
        except:
             print('Este local não existe.')
             return None
    return interna


def adicinar__lista(lista, tarefa=None):
    if tarefa == None:
        tarefa = '<none>'
    lista.append(tarefa)
    return lista


def listar_valores(lista_original, lista_salva):
    for indice,valor in enumerate(lista_original):
        print(f'\t{indice}) {valor}')
    print(f'\nLixeira: ({len(lista_salva)})')


def desfazer(lista_original, lista_salva):
    posicao = input('Digite o indice: ')
    try:
        posicao = int(posicao)
    except:
        posicao = -1
    lista_salva = lista_salva.append(deepcopy(lista_original[posicao]))
    del lista_original[posicao]
    return lista_salva, lista_original



def refazer(lista_original, lista_salva):
    lista_original = lista_original.append(deepcopy(lista_salva[0]))
    del lista_salva[0]
    return lista_original


comando = [listar_valores, desfazer, refazer]


def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe')
        salvar(tarefas, caminho_arquivo)
    return dados


def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False,)
    return dados


CAMINHO_ARQUIVO = 'C:\\Users\\danie\\Documents\\curso_python\\udemy_python\\secao_4_python_intermediario\\10-final_secao_4\\aula119.json'
tarefas_lista = ler([], CAMINHO_ARQUIVO)
tarefas_excluidas = []

while True:

    print('\n\nComandos: [0]listar, [1]desfazer, [2]refazer')
    menu = input('Digite uma tarefa: ')

    print()

    if menu in '012'and 0 <= int(menu) <=2:

        a = executar_funcao(comando[int(menu)])
        a(lista_original = tarefas_lista, lista_salva = tarefas_excluidas)
        continue

    b = executar_funcao(adicinar__lista)
    b(tarefa = menu, lista = tarefas_lista)

    print('Tarefa Adinionada')     
    salvar(tarefas_lista, CAMINHO_ARQUIVO)    
