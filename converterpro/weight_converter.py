THOUSAND = 1e3
MILLION = 1e6
BILLION = 1e9
TRILLION = 1e12
KILOGRAMS_TO_POUNDS = 2.2046226218488
MILLIGRAMS_TO_POUNDS = 453592.37
MILLIGRAMS_TO_OUNCES = 28349.523125

class Gram():

    def __init__(self, value):
        self.value = value

    def convert_to_grams(self):
        return self.value
    
    def convert_to_milligrams(self):
        return self.value * THOUSAND

    def convert_to_kilograms(self):
        return self.value / THOUSAND

class Milligram():

    def __init__(self, value):
        self.value = value

    def convert_to_grams(self):
        return self.value / THOUSAND
    
    def convert_to_milligrams(self):
        return self.value 
    
    def convert_to_kilograms(self):
        return self.value / MILLION
    
    def convert_to_pounds(self):
        return self.value / MILLIGRAMS_TO_POUNDS
    
    def convert_to_pounds(self):
        return self.value / MILLIGRAMS_TO_OUNCES

class Kilogram():

    def __init__(self, value):
        self.value = value

    def convert_to_grams(self):
        return self.value * THOUSAND
    
    def convert_to_milligrams(self):
        return self.value * MILLION
    
    def convert_to_kilograms(self):
        return self.value
    
    def convert_to_pounds(self):
        return self.value * KILOGRAMS_TO_POUNDS