import unittest
from format_price import format_price


class TestFormatPrice(unittest.TestCase):

    def test_float_without_fraction(self):
        self.assertEqual(format_price('3435.0000000'), '3 435')

    def test_float_with_fraction(self):
        self.assertEqual(format_price('555555.565656565'), '555 555.57')

    def test_int(self):
        self.assertEqual(format_price('1234567890'), '1 234 567 890')


if __name__ == '__main__':
    unittest.main()
