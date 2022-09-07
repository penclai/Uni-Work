from sandboxes.cl17286.ManualUnitTesting.BankAccountRefactored import BankAccount

# class BankAccountTest:
#     def __init__(self):
#         pass

def test_creation():
    a = BankAccount(100.0, 31, 0.0001)
    assert a.balance == 100.0, "Incorrect balance!"
    assert a.interestRate == 0.0001
    assert a.dayLastOp == 31
    assert a.interestEarned == 0


def test_deposit():
    a = BankAccount(100.0, 31, 0.0001)
    a.deposit(50, 61)
    assert a.balance == 150.0, "Incorrect balance!"
    assert a.interestEarned == 0.3, "Incorrect interest!"
    assert a.dayLastOp == 61, "Incorrect day of last operation!"


def test_withdrawal():
    a = BankAccount(100.0, 31, 0.0001)
    a.withdraw(50, 61)
    assert a.balance == 50.0, "Incorrect balance!"
    assert a.interestEarned == 0.3, "Incorrect interest!"
    assert a.dayLastOp == 61, "Incorrect day of last operation!"


def test_addInterestToBalance():
    a = BankAccount(100.0, 31, 0.0001)
    a.deposit(50, 61)
    a.addInterestToBalance()
    assert a.balance == 150.3, "Incorrect balance!"
    assert a.interestEarned == 0, "Incorrect interest!"


# def main():
#     # Now we invoke the tests
#     BankAccountTest.test_creation()
#     BankAccountTest.test_deposit()
#     BankAccountTest.test_withdrawal()
#     BankAccountTest.test_addInterestToBalance()
#     print("Success!")

def main():
    # Now we invoke the tests
    test_creation()
    test_deposit()
    test_withdrawal()
    test_addInterestToBalance()
    print("Success!")


if __name__ == "__main__":
    main()
