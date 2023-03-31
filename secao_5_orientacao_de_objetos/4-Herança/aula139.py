# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

# class MinhaString(str):

#     def upper(self):

#         print('Chamou UPPER')
#         return super(MinhaString, self).upper()
    


# string = MinhaString('Daniel')
# print(string.upper())


class A:
    atribruto_a = 'valor A'

    def __init__(self, atributo):
        self.atribruto = atributo


    def metodo(self):
        print('A')

class B(A):
    atribruto_b = 'valor B'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')

class C(B):
    atribruto_c = 'valor C'

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        print('^^^ Subindo para B ^^^')


    def metodo(self):
        # super().metodo              # B
        # super(B, self).metodo()     # A
      # super(A, self).metodo()     # OBJECT  # !!!NÃO POSSUI!!!
        print('C')

c = C('Atributo', 'TESTE')
print(c.atribruto)
print(c.outra_coisa)
# print(A.mro())
# print(B.mro())
# print(C.mro())


# print(a.atribruto_a)

# print(b.atribruto_a)
# print(b.atribruto_b)

print(c.atribruto_a)
print(c.atribruto_b)
print(c.atribruto_c)

c.metodo()