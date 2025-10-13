import unittest
from coffee_menu import CoffeeMenu


class TestCoffeeMenu(unittest.TestCase):
    def setUp(self):
        self.coffee_menu = CoffeeMenu()

    def tearDown(self):
        self.coffee_menu = None

    def test_get_price_existing_item(self):
        self.assertEqual(self.coffee_menu.menu['latte'], 2.75)

    def test_get_price_non_existing_item(self):
        with self.assertRaises(KeyError):
            self.coffee_menu.menu['caramel machiatto']


if __name__ == '__main__':
    unittest.main()
