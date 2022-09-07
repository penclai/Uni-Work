class BankAccount:
    def __init__(self, initialBalance, dayCreated, interestRate):
        self.balance = initialBalance
        self.dayLastOp = dayCreated
        self.interestRate=interestRate
        self.interestEarned = 0.0

    def deposit(self, amount, dayDeposited ):
        daysInterest = dayDeposited - self.dayLastOp
        self.interestEarned += daysInterest * self.interestRate * self.balance
        self.balance += amount
        self.dayLastOp = dayDeposited

    def withdraw(self, amount, dayWithdrawn):
        daysInterest = dayWithdrawn - self.dayLastOp
        self.interestEarned += daysInterest * self.interestRate * self.balance
        self.balance -= amount
        self.dayLastOp = dayWithdrawn

    def addInterestToBalance(self):
        self.balance += self.interestEarned
        self.interestEarned = 0

def test_creation():
    a = BankAccount(100.0,31,0.0001)
    assert a.balance==100.0, "Incorrect balance!"
    assert a.interestRate==0.0001
    assert a.dayLastOp==31
    assert a.interestEarned==0

def test_deposit():
    a = BankAccount(100.0,31,0.0001)
    a.deposit(50,61)
    assert a.balance==150.0, "Incorrect balance!"
    assert a.interestEarned==0.3, "Incorrect interest!"
    assert a.dayLastOp == 61, "Incorrect day of last operation!"

def test_withdrawal():
    a = BankAccount(100.0,31,0.0001)
    a.withdraw(50,61)
    assert a.balance==50.0, "Incorrect balance!"
    assert a.interestEarned==0.3, "Incorrect interest!"
    assert a.dayLastOp == 61, "Incorrect day of last operation!"

def test_addInterestToBalance():
    a = BankAccount(100.0,31,0.0001)
    a.deposit(50,61)
    a.addInterestToBalance()
    assert a.balance==150.3, "Incorrect balance!"
    assert a.interestEarned==0, "Incorrect interest!"

# Now we invoke the tests
test_creation()
test_deposit()
test_withdrawal()
test_addInterestToBalance()
print("Success!")

