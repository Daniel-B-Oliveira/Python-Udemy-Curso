# __new__ e __init__ em classes Python
# __new__ é o método responsável por criar e
# retornar o novo objeto. Por isso, new recebe cls.
# __new__ ❗️DEVE retornar o novo objeto❗️
# __init__ é o método responsável por inicializar
# a instância. Por isso, init recebe self.
# __init__ ❗️NÃO DEVE retornar nada (None)❗️
# object é a super classe de uma classe

class A:

    def __new__(cls, *arg, **kwags):
        intance_ = super().__new__(cls)
        return intance_


    def __init__(self, x):
        self.x = x
        print('Sou init')
    
    def __repr__(self):
        return 'A()'
    

a = A(x=123)
print(a)
# a = object.__new__(A)
# a.__init__()
# print(a)

