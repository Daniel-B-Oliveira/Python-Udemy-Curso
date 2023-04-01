import accounts

class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._nome

    @name.setter
    def name(self, nome: str):
        self._nome = nome

    @property
    def age(self):
        return self._idade

    @age.setter
    def age(self, idade: int):
        self._idade = idade

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.name!r}, {self.age!r})'
        return f'{class_name}: {attrs}'


class Client(Person):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.account: accounts.Account | None = None


if __name__ == '__main__':
    c1 = Client('Luiz', 30)
    c1.account = accounts.CheckingAccount(111, 222)
    print(c1)
    print(c1.account)
    c2 = Client('Maria', 18)
    c2.account = accounts.SavingsAcconut(112, 223)
    print(c2)
    print(c2.account)