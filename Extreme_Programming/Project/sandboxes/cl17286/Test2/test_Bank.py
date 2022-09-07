from unittest import TestCase
from datetime import date, timedelta
from sandboxes.cl17286.Test2.Bank import Bank
from sandboxes.cl17286.Test2.BankAccount import InsufficientFunds


class test_Bank(TestCase):
    def setUp(self):
        self.b = Bank()
        self.b.createAccount("Aiden Pearce", 100, 0.0015)

    def test_creation(self):
        a = self.b.currentAccount["Aiden Pearce"]
        self.assertAlmostEqual(100, a.balance)
        self.assertEqual(date.today(), a.dayLastOp)
        self.assertAlmostEqual(0, a.interestEarned)

    def test_deposit(self):
        self.b.deposit("Aiden Pearce", 50)
        self.assertAlmostEqual(150, self.b.currentAccount['Aiden Pearce'].balance)
        self.assertAlmostEqual(0, self.b.currentAccount['Aiden Pearce'].interestEarned)
        for i in range(15):
            self.b.nextDay()
        self.b.deposit("Aiden Pearce", 50)
        self.assertAlmostEqual(200,self.b.currentAccount["Aiden Pearce"].balance)
        self.assertAlmostEqual(3.375,self.b.currentAccount["Aiden Pearce"].interestEarned)

    def test_withdraw(self):
        self.b.withdraw("Aiden Pearce", 50)
        self.assertAlmostEqual(50, self.b.currentAccount["Aiden Pearce"].balance)
        with self.assertRaises(InsufficientFunds):
            self.b.withdraw("Aiden Pearce", 200)

    def test_credit_interest(self):
        for i in range(30):
            self.b.nextDay()
        self.b.credit_interest()
        self.assertAlmostEqual(104.5, self.b.currentAccount["Aiden Pearce"].balance)
        self.assertAlmostEqual(0, self.b.currentAccount["Aiden Pearce"].interestEarned)

