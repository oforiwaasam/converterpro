import unittest

from converterpro.weight_converter import Kilogram

class TestWeightConverter(unittest.TestCase):

    def constructor(self):
        self.kilogram = Kilogram(1.0)

    def kilogram_test(self):
        test = self.kilogram
        self.assertEquals(1.0, test.to_kilogram(), result='Expected: 1.0')
        self.assertEquals(1000.0, test.to_gram(), result='Expected: 1000.0')