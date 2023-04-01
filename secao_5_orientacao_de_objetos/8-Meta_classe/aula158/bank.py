import accounts, persons


class Bank:
    def __init__(
    self,
    branch: list[int] | None = None,
    clients: list[persons.Person] | None = None,
    accounts: list[accounts.Account] | None= None,                       
    ):
        self.branch = branch or []
        self.clients = clients or []
        self.accounts = accounts or []


    def branch_check(self, account):
        if account.branch in self.branch:
            print('Branch: check')
            return True
        print('Branch: rejected')
        return False

    def client_check(self, client):
        if client in self.clients:
            print('Client: check')
            return True
        print('Client: rejected')
        return False

    def account_check(self, account):
        if account in self.accounts:
            print('Account: check')
            return True
        print('Account: rejected')
        return False


    def _checa_se_conta_e_do_cliente(self, client, account):
        if account is client.account:
            print('_checa_se_conta_e_do_cliente', True)
            return True
        print('_checa_se_conta_e_do_cliente', False)
        return False


    def authentication (self, client: persons.Person, account: accounts.Account):
        return self.branch_check(account) and \
        self.client_check(client) and\
        self.account_check(account) and\
        self._checa_se_conta_e_do_cliente(client, account)
    

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.branch!r} - {self.clients!r} - {self.accounts!r})'
        return f'{class_name} - {attrs}'



# if __name__ == '__main__':
#     c1 = persons.Client('Daniel', 30)
#     c1.account = accounts.CheckingAccount(111, 222)
#     c2 = persons.Client('Maria', 18)
#     c2.account = accounts.SavingsAcconut(112, 223)

#     bank = Bank()
#     bank.clients.extend([c1, c2])
#     bank.accounts.extend([c1.account, c2.account])
#     bank.branch.extend([111, 222])

#     print(bank.authentication(c1, c1.account))

#     print(c1)
#     print(c1.account)
#     print(c1.__dict__)

#     print(bank)

if __name__ == '__main__':
    c1 = persons.Client('Luiz', 30)
    cc1 = accounts.CheckingAccount(111, 111)

    c1.account = cc1
    c2 = persons.Client('Maria', 18)
    cp1 = accounts.SavingsAcconut(111, 111)
    c2.account = cp1
    banco = Bank()
    banco.clients.extend([c1, c2])
    banco.accounts.extend([cc1, cp1])
    banco.branch.extend([111, 222])

    print(c1.__dict__)

    banco.authentication(c1, cc1)
