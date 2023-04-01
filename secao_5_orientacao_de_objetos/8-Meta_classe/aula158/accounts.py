from abc import ABC, abstractmethod


class Account(ABC):

    def __init__(self, branch:int, account_number:int) -> None:
        self.__balance = 000
        self.branch = branch
        self.account_number = account_number

    # @abstractmethod

    def withdraw(self, value: float) -> float|None: 

        init = self.__balance * (-1)
        
        self.__balance -= value

        if type(self) == SavingsAcconut and self.__balance < 0:

            print('insufficient funds')
            self.__balance += value
            return  None # self.__balance

        if type(self) == CheckingAccount and\
        self.__balance < init*0.1:
            
            print('insufficient funds')
            self.__balance += value
            return  None # self.__balance
        
        print('withdrawal successful')

        return self.__balance


    def deposit(self, value: float) -> float:
        self.__balance += value
        print('deposit successful')
        return self.__balance    



    def balance(self):
        return self.__balance
            


    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.branch!r} - {self.account_number!r} - R${self.__balance!r})'
        return f'{class_name} - {attrs}'


class CheckingAccount(Account):

    def __init__(self, branch, account_number):
        super().__init__(branch, account_number)

    def deposit(self, value):
        return super().deposit(value)
    
    def withdraw(self, value):
        return super().withdraw(value)


class SavingsAcconut(Account):
    def __init__(self, branch, account_number):
        super().__init__(branch, account_number)
    

    def deposit(self, value):
        return super().deposit(value)
    
    def withdraw(self, value):
        return super().withdraw(value)      


