"""
Closure e funções que retornam outras funções
"""

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar  # retirada dos () guarda a ação da função na memória 

# falar_bom_dia = criar_saudacao('Bom dia')
# falar_boa_noite = criar_saudacao('Bom noite')

# nomes = ['Daniel', 'Luiz', 'Otto', 'Selma']

# for nome in nomes:
#     print(falar_bom_dia(nome))

# for nome in nomes:
#     print(falar_boa_noite(nome))

# !!! MDS que LEGAL !!!

falas = ['Bom dia', 'Boa terde', 'Boa noite', 'Boa Madrugada']
nomes = ['Daniel', 'Luiz', 'Otto', 'Selma', 'Pedro', 'Marcius']

for horario in falas:
    falar_horario = criar_saudacao(horario)
    for nome in nomes:
        print(falar_horario(nome))