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


    def compatibility_check(self, client, account):
        if account is client.account:
            print('Compatibility: check')
            return True
        print('Compatibility rejected')
        return False


    def authentication (self, client: persons.Person, account: accounts.Account):
        if self.branch_check(account) and \
        self.client_check(client) and\
        self.account_check(account) and\
        self.compatibility_check(client, account):
            return('all IDs checked; free access')
        return('all IDs checked; access denied')

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
#     c1.account.deposit(123)
#     c1.account.withdraw(120)

