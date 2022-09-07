from sandboxes.cl17286.Test2.BankAccount import BankAccount
from datetime import date, timedelta


class Bank():
    def __init__(self):
        self.currentAccount = {}
        self.todayDate = date.today()
        self.firstAccountNumber = 0

    def createAccount(self, holder, startingBallance, interestRate):
        a = BankAccount(holder, self.firstAccountNumber, startingBallance, self.todayDate, interestRate)
        self.currentAccount[holder] = a

    def deposit(self, holder, amount):
        self.currentAccount[holder].deposit(amount, self.todayDate)

    def nextDay(self):
        self.todayDate += timedelta(days=1)

    def withdraw(self, holder, amount):
        self.currentAccount[holder].withdraw(amount,self.todayDate)

    def credit_interest(self):
        for a in self.currentAccount.values():
            a.UpdateInterestEarn(self.todayDate)
            a.CreditInterest()


