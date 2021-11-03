import unittest
from expense import new_expense, new_expense_test


class TestExpense(unittest.TestCase):

    def test_add_expense(self):
        self.assertEqual(new_expense_test(23, 'toto', 'pchojka'), True)
        self.assertEqual(new_expense_test('bonjour', 23, 23), False)


if __name__ == '__main__':
    unittest.main()
