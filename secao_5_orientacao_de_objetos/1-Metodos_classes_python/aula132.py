
# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.
# atributos que começam com 1 ou 2 underlines
# não devem ser usados fora da classe
#  🐍🤓🤯🤯🤯🤯

class Caneta:
    def __init__(self, cor, cor_tampa = None):
        # private #protect                                      #public  ---> encapsulamento
        self._cor = cor  # Não use este atributo, convenção.
        self._cor_tampa = cor_tampa


    @property       # obter o valor
    def cor(self):
        return self._cor
    

    @property
    def cor_tampa(self):
        return self._cor_tampa


    @cor.setter     # configurar o valor
    def cor(self, valor):
        self._cor = valor


    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor





caneta = Caneta('azul')
caneta.cor_tampa = 'branca'
print(caneta.cor_tampa)
caneta.cor = 'azul'
# getter = obter valor
print(caneta.cor)

