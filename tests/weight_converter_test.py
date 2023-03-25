import unittest

from converterpro import Gram, Milligram, Kilogram

THOUSAND = 1e3
MILLION = 1e6


class TestWeightConverter(unittest.TestCase):
    def test_gram(self):
        test = Gram(1.0)
        self.assertEqual(1.0, test.convert_to_grams(), "Expects a float or 1.0")
        self.assertEqual(THOUSAND, test.convert_to_milligrams(), "Expects a float or 1000.0")
        self.assertEqual(0.001, test.convert_to_kilograms(), "Expects a float or 0.001")
        self.assertEqual(1e-6, test.convert_to_metric_tonnes(), "Expects a float or 0.000001")
        self.assertEqual(9.842065276110607e-07, test.convert_to_imperial_tons(), "Expects a float or 9.842065276110607e-07")
        self.assertEqual(1.102311310924388e-06, test.convert_to_us_tons(), "Expects a float or 1.102311310924388e-06")
        self.assertEqual(0.002204622621848776, test.convert_to_pounds(), "Expects a float or 0.002204622621848776")
        self.assertEqual(0.035273961949580414, test.convert_to_ounces(), "Expects a float or 0.035273961949580414")

    def test_milligram(self):
        test = Milligram(1.0)
        self.assertEqual(0.001, test.convert_to_grams(), "Expects a float or 0.001")
        self.assertEqual(1.0, test.convert_to_milligrams(), "Expects a float or 1.0")
        self.assertEqual(1e-6, test.convert_to_kilograms(), "Expects a float or 1e-6")
        self.assertEqual(1e-9, test.convert_to_metric_tonnes(), "Expects a float or 1e-9")
        self.assertEqual(9.842065276110607e-10, test.convert_to_imperial_tons(), "Expects a float or 9.842065276110607e-10")
        self.assertEqual(1.102311310924388e-09, test.convert_to_us_tons(), "Expects a float or 1.102311310924388e-09")
        self.assertEqual(2.204622621848776e-06, test.convert_to_pounds(), "Expects a float or 2.204622621848776e-06")
        self.assertEqual(3.5273961949580415e-05, test.convert_to_ounces(), "Expects a float or 3.5273961949580415e-05")

    def test_kilogram(self):
        test = Kilogram(1.0)
        self.assertEqual(THOUSAND, test.convert_to_grams(), "Expected: 1000.0")
        self.assertEqual(MILLION, test.convert_to_milligrams(), "Expected 1000000.0")
        self.assertEqual(1.0, test.convert_to_kilograms(), "Expected: 1.0")
        self.assertEqual(2.2046226218488, test.convert_to_pounds(), "Expected 2.2046226218488")


if __name__ == "__main__":
    unittest.main()
