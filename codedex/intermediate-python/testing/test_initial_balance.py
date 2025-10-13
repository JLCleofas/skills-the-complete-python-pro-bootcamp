import unittest
from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.bank_account = BankAccount(100)

    def tearDown(self):
        self.bank_account = None

    def test_balance(self):
        self.assertEqual(self.bank_account.balance, 100)

    def test_deposit_positive_amount(self):
        self.bank_account.deposit(50)
        self.assertEqual(self.bank_account.balance, 150)

    def test_deposit_zero_amount(self):
        with self.assertRaises(ValueError):
            self.bank_account.deposit(0)

    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.bank_account.deposit(-1)

    def test_withdraw_positive_amount(self):
        self.bank_account.withdraw(30)
        self.assertEqual(self.bank_account.balance, 70)

    def test_withdraw_zero_amount(self):
        with self.assertRaises(ValueError):
            self.bank_account.withdraw(0)

    def test_withdraw_negative_amount(self):
        with self.assertRaises(ValueError):
            self.bank_account.withdraw(-1)

    def test_withdraw_insufficient(self):
        with self.assertRaises(ValueError):
            self.bank_account.withdraw(200)


if __name__ == '__main__':
    unittest.main()
