# -*- coding: utf-8 -*-

class BankAccount:
    def __init__(self, balance=0):
        assert isinstance(balance, (float, int))

        if balance < 0:
            raise ValueError("Balance must be zero or positive")

        if balance > 0:
            self.__balance = balance
            self.__account_activities = [balance]

    @property
    def balance(self):
        return self.__balance

    @property
    def account_activities(self):
        return self.__account_activities

    def withdraw(self, amount):
        self.__check_amount(amount)

        if amount > self.balance:
            print("Insufficient balance")
            return
        elif amount == 0:
            return

        self.__balance -= amount
        self.__account_activities.append(-amount)

    def __check_amount(self, amount):
        assert isinstance(amount, (float, int))
        if amount < 0:
            raise ValueError("Amount must be zero or positive")
        return

    def deposit(self, amount):

        self.__check_amount(amount)
        if amount == 0:
            return

        self.__balance += amount
        self.__account_activities.append(amount)


if __name__ == "__main__":
    account = BankAccount(1000)

    account.deposit(12)
    account.withdraw(12)
    account.withdraw(1000)
    account.withdraw(500)

    print(account.account_activities)
    print(account.balance)
