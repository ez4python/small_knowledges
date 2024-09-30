class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount < self._balance:
            self._balance -= amount
        else:
            print('Insufficient funds')

    def get_balance(self):
        return self._balance


# object creation
account = BankAccount('John', 100)

# operations
account.deposit(1000)
account.withdraw(900)
print(account.get_balance())
