import datetime


class BankAccount:
    def __init__(self, accountHolder, accountNumber, initialBalance, dayCreated, interestRate):
        self.accountHolder = accountHolder
        self.accountNumber = accountNumber
        self.balance = initialBalance
        self.dayLastOp = dayCreated
        self.interestRate = interestRate
        self.interestEarned = 0.0

    def deposit(self, amount, dayDeposited):
        self.UpdateInterestEarn(dayDeposited)
        self.balance += amount

    # def withdraw(self, amount, dayWithdrawn):
    #     self.deposit(-amount, dayWithdrawn)
    def withdraw(self, amount, dayWithdrawn):
        if amount > self.balance:
            raise InsufficientFunds(self.balance)
        self.deposit(-amount, dayWithdrawn)

    def CreditInterest(self):
        self.balance += self.interestEarned
        self.interestEarned = 0

    def UpdateInterestEarn(self, dayUpdated):
        daysInterest = (dayUpdated - self.dayLastOp).days
        self.interestEarned += daysInterest * self.interestRate * self.balance
        self.dayLastOp = dayUpdated  #replace the last operation day

class InsufficientFunds(Exception):
    def __init__(self, availableFunds):
        self.availableFunds = availableFunds
    def __str__(self):
        return repr(self.availableFunds)