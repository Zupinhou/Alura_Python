class account:
    def __init__(self, account_id, account_holder_name, account_balance):
        self.__account_id = account_id
        self.__account_holder_name = account_holder_name
        self.__account_balance = account_balance
    
    def deposit(self, amount):
        if amount <= 0:
            print('O valor depositado deve ser positivo!')    
        self.__account_balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print('O valor a ser sacado deve ser positivo!')
        elif self.__account_balance <= amount:
            print('Saldo insuficiente!')
        else:
            self.__account_balance -= amount

    def transfer(self, destination_account, amount):
        self.withdraw(amount)
        destination_account.deposit(amount)
        print(f'A tranferência de {amount:.2f} foi realizada com sucesso!')
    
    def show_account_balance(self):
        print(f'Seu saldo é: {self.__account_balance}')

    def __str__(self):
        return f'Conta:# {self.__account_id}{self.__account_holder_name} | Saldo:{self.__account_balance}'
