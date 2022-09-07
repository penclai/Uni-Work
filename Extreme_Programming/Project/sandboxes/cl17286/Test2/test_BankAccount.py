from unittest import TestCase
from sandboxes.cl17286.Test2.BankAccount import BankAccount, InsufficientFunds
from datetime import date, timedelta
# import datetime

FIFTEEN_DAYS_AFTER_CREATION = date.today() + timedelta(days=15)


class TestBankAccount(TestCase):

    # def __init__(self, date):
    #     self.date = datetime.date.today()

    def setUp(self):
        self.a = self.create_default_bank_account()
        # self.date = datetime.date.today()  #replace with using from datetime import date, timedelta according to Ric video
        # self.day = date()

    def test_creation(self):
        self.assert_account(self.a,100.0, date.today(), 0)
        self.assertEqual(0.0015,self.a.interestRate)

    def test_deposit(self):
        self.a.deposit(50, date.today()+timedelta(days=8))
        self.assert_account(self.a, 150, date.today()+timedelta(days=8), 1.2)

    def test_withdraw(self):
        self.a.withdraw(50, FIFTEEN_DAYS_AFTER_CREATION)
        self.assert_account(self.a, 50, FIFTEEN_DAYS_AFTER_CREATION, 2.25)
        with self.assertRaises(InsufficientFunds):
            self.a.withdraw(200,FIFTEEN_DAYS_AFTER_CREATION)

    def test_add_interest_to_balance(self):
        self.a.UpdateInterestEarn(FIFTEEN_DAYS_AFTER_CREATION)
        self.assert_account(self.a, 100.0, FIFTEEN_DAYS_AFTER_CREATION, 2.25)

    def test_Credit_interest(self):
        self.a.deposit(50, FIFTEEN_DAYS_AFTER_CREATION)
        self.a.CreditInterest()
        self.assert_account(self.a, 152.25, FIFTEEN_DAYS_AFTER_CREATION, 0)

    @staticmethod
    def create_default_bank_account():
        accountHolder = "Aiden Pearce"
        accountNumber = 201320162030
        return BankAccount(accountHolder, accountNumber, 100.0, date.today(), 0.0015)

    def assert_account(self, account, expected_balance, expected_day_last_op, expected_interest_earned):
        self.assertAlmostEqual(expected_balance, self.a.balance)
        self.assertAlmostEqual(expected_interest_earned, self.a.interestEarned)
        self.assertEqual(expected_day_last_op, self.a.dayLastOp)
