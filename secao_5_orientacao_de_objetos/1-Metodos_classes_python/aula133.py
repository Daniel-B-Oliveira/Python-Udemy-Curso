# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.

from functools import partial


class Foo:
    def __init__(self):
        self.public = 'Isso é público'
        self._protected = 'Isso é protegido'
        self.__privated = 'Isso é privado'

    def metodo_publico(self):
        return 'metodo público'
    

    def _metodo_protected(self):
        return 'metodo protegido'


    def __metodo_private(self):
        return 'metodo privado'
    

f = Foo()
print(f.public)
print(f._metodo_protected())
print(f.__metodo_private())

