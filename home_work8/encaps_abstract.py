class BankAccount:
    def __init__(self, balance: float):
        self.__balance = balance  # інкапсуляція балансу

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Сума депозиту має бути більшою за 0")

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Сума зняття має бути більшою за 0")
        if amount > self.__balance:
            raise ValueError("Недостатньо коштів на рахунку")
        self.__balance -= amount

    def get_balance(self):
        return self.__balance

# Використання класу
account = BankAccount(5000)
account.deposit(850)
account.withdraw(300)
print(account.get_balance())  # Виведе 5550
