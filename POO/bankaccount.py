class account:
    def __init__(self, id, name, balance):
        self.__id = id
        self.__name = name
        self.__balance = balance
    
    def deposit(self, amount):
        if amount <= 0:
            print('O valor depositado deve ser positivo!')    
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print('O valor a ser sacado deve ser positivo!')
        elif self.__balance <= amount:
            print('Saldo insuficiente!')
        else:
            self.__balance -= amount
    
    def show_balance(self):
        print(f'Seu saldo é: {self.__balance}')

    def __str__(self):
        return print(f'Conta:#{self.__id}{self.__name} | Saldo:{self.__balance}')
