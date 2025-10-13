import unittest
from string_utils import reverse_string, capitalize_string, is_capitalized


class TestStringUtils(unittest.TestCase):
    def test_reverse(self):
        result = reverse_string('teststring')
        expected_result = 'gnirtstset'
        self.assertEqual(result, expected_result)

    def test_capitalize(self):
        result = capitalize_string('hello')
        expected_result = 'Hello'
        self.assertEqual(result, expected_result)

    def test_is_capitalized(self):
        result = is_capitalized('Test')

        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
