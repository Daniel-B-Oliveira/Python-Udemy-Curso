# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)

class Conection:


    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None
    

    def set_user(self, user):
        self.user = user


    def set_password(self, password):
        self.password = password


    @classmethod
    def create_with_auth(cls, user, password ):
        conection = cls()
        conection.user = user
        conection.password = password
        return conection

    @staticmethod
    def regras(user='novo usuário'):
        print(f'Olá {user}, estas são as seguinte regras de nossos serviços...')



c1 = Conection.create_with_auth('Daniel', 123)
Conection.regras()
# c1.set_user('Daniel')
# c1.set_password('123')
print(c1.user)
print(c1.password)