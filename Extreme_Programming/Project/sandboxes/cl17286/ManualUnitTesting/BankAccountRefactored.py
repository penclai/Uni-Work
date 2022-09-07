class BankAccount:
    def __init__(self, initialBalance, dayCreated, interestRate):
        self.balance = initialBalance
        self.dayLastOp = dayCreated
        self.interestRate=interestRate
        self.interestEarned = 0.0

    def deposit(self, amount, dayDeposited ):
        self.IntrestEarn(dayDeposited)
        self.dayLastOp = dayDeposited
        self.balance += amount

    def withdraw(self, amount, dayWithdrawn):
        self.deposit(-amount, dayWithdrawn)

    def addInterestToBalance(self):
        self.balance += self.interestEarned
        self.interestEarned = 0

    def IntrestEarn(self, dayDeposited):
        daysInterest = dayDeposited - self.dayLastOp
        self.interestEarned += daysInterest * self.interestRate * self.balance



