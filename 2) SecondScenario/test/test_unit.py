from scripts.producedata import Transaction
import unittest


class TestTransaction(unittest.TestCase):

    def test_transaction_len(self):
        transaction = Transaction("2").get_info()
        self.assertEqual(len(transaction), 4)
