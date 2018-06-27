import unittest
from format_price import format_price


class TestFormatPrice(unittest.TestCase):

    def test_string_of_float(self):
        self.assertEqual(format_price('123456.123456'), '123 456.12')

    def test_float_without_fraction(self):
        self.assertEqual(format_price(123456.000000), '123 456')

    def test_float_with_fraction(self):
        self.assertEqual(format_price(123456.123456), '123 456.12')

    def test_int(self):
        self.assertEqual(format_price(123456), '123 456')

    def test_bin_string_of_float(self):
        self.assertEqual(format_price(b'123456.12'), '123 456.12')

    def test_float_with_letter_in_string(self):
        self.assertIsNone(format_price('123abc.123abc'))

    def test_string_of_number_with_duble_dot(self):
        self.assertIsNone(format_price('123.456.000'))

    def test_isinstance(self):
        self.assertIsInstance(format_price(123456), str)

    def test_price_is_list_of_number(self):
        self.assertIsNone(format_price([1, 2, 3, 4, 5, 6]))

    def test_price_is_dict(self):
        self.assertIsNone(format_price({'price': 123.456}))

    def test_price_is_set_of_string(self):
        self.assertIsNone(format_price(('123.456', '123.456')))

    def test_price_is_str_of_number_with_many_zero(self):
        self.assertEqual(format_price('123456.000000000'), '123 456')

    def test_result_not_none(self):
        self.assertIsNotNone(format_price('123456'))

    def test_price_is_boolean_true(self):
        self.assertIsNone(format_price(True))

    def test_price_is_boolean_false(self):
        self.assertIsNone(format_price(False))

    def test_price_object_is_none(self):
        self.assertIsNone(format_price(None))


if __name__ == '__main__':
    unittest.main()
