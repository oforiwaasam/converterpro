import unittest

from converterpro.weight_converter import Gram, Kilogram

THOUSAND = 1e3
MILLION = 1e6


class TestWeightConverter(unittest.TestCase):

    def constructor(self):
        self.kilograms = Kilogram(1.0)
        self.grams = Gram(1.0)

    def test_gram(self):
        test = self.grams
        self.assertEqual(1.0, test.convert_to_grams(),
                         'Expects a float or 1.0')
        self.assertEqual(THOUSAND, test.convert_to_milligrams(),
                         'Expects a float or 1000.0')
        self.assertEqual(0.001, test.convert_to_kilograms(),
                         'Expects a float or 0.001')

    def test_kilogram(self):
        test = self.kilograms
        self.assertEqual(THOUSAND, test.convert_to_grams(), 'Expected: 1000.0')
        self.assertEqual(1.0, test.convert_to_kilograms(), 'Expected: 1.0')
        self.assertEqual(MILLION, test.convert_to_milligrams(),
                         'Expected 1000000.0')
        self.assertEqual(2.2046226218488, test.convert_to_pounds,
                         'Expected 2.2046226218488')


if __name__ == '__main__':
    unittest.main()
