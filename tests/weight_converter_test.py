import unittest

# from converterpro import Gram, Milligram, Kilogram, MetricTonnes, ImperialTons, USTons
from converterpro import weight_converter

THOUSAND = 1e3
MILLION = 1e6


class TestWeightConverter(unittest.TestCase):
    def test_gram(self):
        test = weight_converter.Gram(1.0)
        self.assertEqual(1.0, test.convert_to_grams(), "Expects a float or 1.0")
        self.assertEqual(THOUSAND, test.convert_to_milligrams(), "Expects a float or 1000.0")
        self.assertEqual(0.001, test.convert_to_kilograms(), "Expects a float or 0.001")
        self.assertEqual(1e-6, test.convert_to_metric_tonnes(), "Expects a float or 0.000001")
        self.assertEqual(9.842065276110607e-07, test.convert_to_imperial_tons(), "Expects a float or 9.842065276110607e-07")
        self.assertEqual(1.102311310924388e-06, test.convert_to_us_tons(), "Expects a float or 1.102311310924388e-06")
        self.assertEqual(0.002204622621848776, test.convert_to_pounds(), "Expects a float or 0.002204622621848776")
        self.assertEqual(0.035273961949580414, test.convert_to_ounces(), "Expects a float or 0.035273961949580414")

    def test_milligram(self):
        test = weight_converter.Milligram(1.0)
        self.assertEqual(0.001, test.convert_to_grams(), "Expects a float or 0.001")
        self.assertEqual(1.0, test.convert_to_milligrams(), "Expects a float or 1.0")
        self.assertEqual(1e-6, test.convert_to_kilograms(), "Expects a float or 1e-6")
        self.assertEqual(1e-9, test.convert_to_metric_tonnes(), "Expects a float or 1e-9")
        self.assertEqual(9.842065276110607e-10, test.convert_to_imperial_tons(), "Expects a float or 9.842065276110607e-10")
        self.assertEqual(1.102311310924388e-09, test.convert_to_us_tons(), "Expects a float or 1.102311310924388e-09")
        self.assertEqual(2.204622621848776e-06, test.convert_to_pounds(), "Expects a float or 2.204622621848776e-06")
        self.assertEqual(3.5273961949580415e-05, test.convert_to_ounces(), "Expects a float or 3.5273961949580415e-05")

    def test_kilogram(self):
        test = weight_converter.Kilogram(1.0)
        self.assertEqual(THOUSAND, test.convert_to_grams(), "Expects a float or 1000.0")
        self.assertEqual(MILLION, test.convert_to_milligrams(), "Expects a float or 1000000.0")
        self.assertEqual(1.0, test.convert_to_kilograms(), "Expects a float or 1.0")
        self.assertEqual(0.001, test.convert_to_metric_tonnes(), "Expects a float or 0.001")
        self.assertEqual(0.0009842065276110606, test.convert_to_imperial_tons(), "Expects a float or 0.0009842065276110606")
        self.assertEqual(0.001102311310924388, test.convert_to_us_tons(), "Expects a float or 0.001102311310924388")
        self.assertEqual(2.2046226218488, test.convert_to_pounds(), "Expects a float or 2.2046226218488")
        self.assertEqual(35.27396194958, test.convert_to_ounces(), "Expects a float or 35.27396194958")

    def test_metric_tonnes(self):
        test = weight_converter.MetricTonnes(1.0)
        self.assertEqual(1e6, test.convert_to_grams(), "Expects a float or 1000000.0")
        self.assertEqual(1e9, test.convert_to_milligrams(), "Expects a float or 1000000000.0")
        self.assertEqual(1000.0, test.convert_to_kilograms(), "Expects a float or 1000.0")
        self.assertEqual(1.0, test.convert_to_metric_tonnes(), "Expects a float or 1.0")
        self.assertEqual(0.9842065276110608, test.convert_to_imperial_tons(), "Expects a float or 0.9842065276110608")
        self.assertEqual(1.1023113109244, test.convert_to_us_tons(), "Expects a float or 1.1023113109244")
        self.assertEqual(2204.6226218488, test.convert_to_pounds(), "Expects a float or 2204.6226218488")
        self.assertEqual(35273.96194958, test.convert_to_ounces(), "Expects a float or 35273.96194958")

    def test_imperial_tons(self):
        test = weight_converter.ImperialTons(1.0)
        self.assertEqual(1016046.9088, test.convert_to_grams(), "Expects a float or 1016046.9088")
        self.assertEqual(1016046908.8, test.convert_to_milligrams(), "Expects a float or 1016046908.8")
        self.assertEqual(1016.0469088, test.convert_to_kilograms(), "Expects a float or 1016.0469088")
        self.assertEqual(1.0160469088, test.convert_to_metric_tonnes(), "Expects a float or 1.0160469088")
        self.assertEqual(1.0, test.convert_to_imperial_tons(), "Expects a float or 1.0")
        self.assertEqual(1.12, test.convert_to_us_tons(), "Expects a float or 1.12")
        self.assertEqual(2240, test.convert_to_pounds(), "Expects a float or 2240")
        self.assertEqual(35840, test.convert_to_ounces(), "Expects a float or 35840")

    def test_us_tons(self):
        test = weight_converter.USTons(1.0)
        self.assertEqual(907184.74, test.convert_to_grams(), "Expects a float or 907184.74")
        self.assertEqual(907184740, test.convert_to_milligrams(), "Expects a float or 907184740")
        self.assertEqual(907.18474, test.convert_to_kilograms(), "Expects a float or 907.18474")
        self.assertEqual(0.90718473999999, test.convert_to_metric_tonnes(), "Expects a float or 0.90718473999999")
        self.assertEqual(0.8928571428571428, test.convert_to_imperial_tons(), "Expects a float or 0.8928571428571428")
        self.assertEqual(1.0, test.convert_to_us_tons(), "Expects a float or 1.0")
        self.assertEqual(2000, test.convert_to_pounds(), "Expects a float or 2000")
        self.assertEqual(32000, test.convert_to_ounces(), "Expects a float or 32000")

    def test_pounds(self):
        test = weight_converter.Pounds(1.0)
        self.assertEqual(453.59237, test.convert_to_grams(), "Expects a float or 453.59237")
        self.assertEqual(453592.37, test.convert_to_milligrams(), "Expects a float or 453592.37")
        self.assertEqual(0.453592369999995, test.convert_to_kilograms(), "Expects a float or 0.453592369999995")
        self.assertEqual(0.000453592369999995, test.convert_to_metric_tonnes(), "Expects a float or 0.000453592369999995")
        self.assertEqual(0.0004464285714285714, test.convert_to_imperial_tons(), "Expects a float or 0.0004464285714285714")
        self.assertEqual(0.0005, test.convert_to_us_tons(), "Expects a float or 0.0005")
        self.assertEqual(1.0, test.convert_to_pounds(), "Expects a float or 1.0")
        self.assertEqual(16, test.convert_to_ounces(), "Expects a float or 16")

    def test_ounces(self):
        test = weight_converter.Ounces(1.0)
        self.assertEqual(28.349523125, test.convert_to_grams(), "Expects a float or 28.349523125")
        self.assertEqual(28349.523125, test.convert_to_milligrams(), "Expects a float or 28349.523125")
        self.assertEqual(0.028349523125000334, test.convert_to_kilograms(), "Expects a float or 0.028349523125000334")
        self.assertEqual(2.834952312500033e-05, test.convert_to_metric_tonnes(), "Expects a float or 2.834952312500033e-05")
        self.assertEqual(2.7901785714285713e-05, test.convert_to_imperial_tons(), "Expects a float or 2.7901785714285713e-05")
        self.assertEqual(3.125e-05, test.convert_to_us_tons(), "Expects a float or 3.125e-05")
        self.assertEqual(0.0625, test.convert_to_pounds(), "Expects a float or 0.0625")
        self.assertEqual(1.0, test.convert_to_ounces(), "Expects a float or 1.0")


if __name__ == "__main__":
    unittest.main()
