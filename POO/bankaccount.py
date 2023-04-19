class account:
    def __init__(self, account_id, account_holder_name, account_balance):
        self.__account_id = account_id
        self.__account_holder_name = account_holder_name
        self.__account_balance = account_balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('O valor depositado deve ser positivo!')
        self.__account_balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('O valor a ser sacado deve ser positivo!')
        elif self.__account_balance <= amount:
            raise ValueError('Saldo insuficiente!')
        else:
            self.__account_balance -= amount

    def transfer(self, destination_account, amount):
        if self.__account_id == destination_account.get_account_id():
            raise ValueError('Não é possível transferir para a mesma conta!')
        self.withdraw(amount)
        destination_account.deposit(amount)
        print(f'A tranferência de {amount:.2f} foi realizada com sucesso!')
    
    def show_account_balance(self):
        print(f'Seu saldo é: {self.__account_balance}')
    
    @property
    def account_id(self):
        return self.__account_id
    
    @property
    def account_holder_name(self):
        return self.__account_holder_name
    
    @property
    def account_balance(self):
        return self.__account_balance
