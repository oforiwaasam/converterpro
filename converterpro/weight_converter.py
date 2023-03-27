
THOUSAND = 1e3
MILLION = 1e6
BILLION = 1e9
TRILLION = 1e12

#Constants for weight conversion

GRAMS_TO_POUNDS = 453.59237
GRAMS_TO_OUNCES = 28.349523125
GRAMS_TO_US_TONS = 907184.74
GRAMS_TO_IMPERIAL_TONS = 1016046.9088

MILLIGRAMS_TO_POUNDS = 453592.37
MILLIGRAMS_TO_OUNCES = 28349.523125
MILLIGRAMS_TO_US_TONS = 907184740
MILLIGRAMS_TO_IMPERIAL_TONS = 1016046908.8

KILOGRAMS_TO_POUNDS = 2.2046226218488
KILOGRAMS_TO_OUNCES = 35.27396194958
KILOGRAMS_TO_US_TONS = 907.18474
KILOGRAMS_TO_IMPERIAL_TONS = 1016.0469088

METRIC_TONNES_TO_IMPERIAL_TONS = 1.0160469088
METRIC_TONNES_TO_US_TONS = 1.1023113109244
METRIC_TONNES_TO_POUNDS = 2204.6226218488
METRIC_TONNES_TO_OUNCES = 35273.96194958

IMPERIAL_TONS_TO_US_TONS = 1.12
IMPERIAL_TONS_TO_POUNDS = 2240
IMPERIAL_TONS_TO_OUNCES = 35840

US_TONS_TO_POUNDS = 2000
US_TONS_TO_OUNCES = 32000


# Classes for different units of mass in the metric system

# Grams
class Gram:
    def __init__(self, value):
        self.value = value

    def convert_to_grams(self):
        return self.value

    def convert_to_milligrams(self):
        return self.value * THOUSAND

    def convert_to_kilograms(self):
        return self.value / THOUSAND

    def convert_to_metric_tonnes(self):
        return self.value / MILLION

    def convert_to_imperial_tons(self):
        return self.value / GRAMS_TO_IMPERIAL_TONS

    def convert_to_us_tons(self):
        return self.value / GRAMS_TO_US_TONS

    def convert_to_pounds(self):
        return self.value / GRAMS_TO_POUNDS

    def convert_to_ounces(self):
        return self.value / GRAMS_TO_OUNCES

# Milligrams
class Milligram:
    def __init__(self, value):
        self.value = value

    def convert_to_grams(self):
        return self.value / THOUSAND

    def convert_to_milligrams(self):
        return self.value

    def convert_to_kilograms(self):
        return self.value / MILLION

    def convert_to_metric_tonnes(self):
        return self.value / BILLION

    def convert_to_imperial_tons(self):
        return self.value / MILLIGRAMS_TO_IMPERIAL_TONS

    def convert_to_us_tons(self) -> float:
        return self.value / MILLIGRAMS_TO_US_TONS

    def convert_to_pounds(self):
        return self.value / MILLIGRAMS_TO_POUNDS

    def convert_to_ounces(self):
        return self.value / MILLIGRAMS_TO_OUNCES

# Kilograms
class Kilogram:
    def __init__(self, value):
        self.value = value

    def convert_to_grams(self):
        return self.value * THOUSAND

    def convert_to_milligrams(self):
        return self.value * MILLION

    def convert_to_kilograms(self):
        return self.value

    def convert_to_metric_tonnes(self):
        return self.value / THOUSAND

    def convert_to_imperial_tons(self):
        return self.value / KILOGRAMS_TO_IMPERIAL_TONS

    def convert_to_us_tons(self):
        return self.value / KILOGRAMS_TO_US_TONS

    def convert_to_pounds(self):
        return self.value * KILOGRAMS_TO_POUNDS

    def convert_to_ounces(self):
        return self.value * KILOGRAMS_TO_OUNCES

# Metric Tonnes
class MetricTonnes:
    def __init__(self, value):
        self.value = value

    def convert_to_grams(self):
        return self.value * MILLION

    def convert_to_milligrams(self):
        return self.value * BILLION

    def convert_to_kilograms(self):
        return self.value * THOUSAND

    def convert_to_metric_tonnes(self):
        return self.value

    def convert_to_imperial_tons(self):
        return self.value / METRIC_TONNES_TO_IMPERIAL_TONS

    def convert_to_us_tons(self):
        return self.value * METRIC_TONNES_TO_US_TONS

    def convert_to_pounds(self):
        return self.value * METRIC_TONNES_TO_POUNDS

    def convert_to_ounces(self):
        return self.value * METRIC_TONNES_TO_OUNCES


# UK TONS / IMPERIAL TONS
class ImperialTons:
    def __init__(self, value):
        self.value = value

    def convert_to_grams(self):
        return self.value * GRAMS_TO_IMPERIAL_TONS

    def convert_to_milligrams(self):
        return self.value * MILLIGRAMS_TO_IMPERIAL_TONS

    def convert_to_kilograms(self):
        return self.value * KILOGRAMS_TO_IMPERIAL_TONS

    def convert_to_metric_tonnes(self):
        return self.value * METRIC_TONNES_TO_IMPERIAL_TONS

    def convert_to_imperial_tons(self):
        return self.value

    def convert_to_us_tons(self) -> float:
        return self.value * IMPERIAL_TONS_TO_US_TONS

    def convert_to_pounds(self) -> float:
        return self.value * IMPERIAL_TONS_TO_POUNDS

    def convert_to_ounces(self) -> float:
        return self.value * IMPERIAL_TONS_TO_OUNCES


# US TONS
class USTons:
    def __init__(self, value):
        self.value = value

    def convert_to_us_tons(self):
        return self.value

    def convert_to_grams(self):
        return self.value * GRAMS_TO_US_TONS

    def convert_to_milligrams(self):
        return self.value * MILLIGRAMS_TO_US_TONS

    def convert_to_kilograms(self):
        return self.value * KILOGRAMS_TO_US_TONS

    def convert_to_metric_tonnes(self):
        return self.value / METRIC_TONNES_TO_US_TONS

    def convert_to_imperial_tons(self):
        return self.value / IMPERIAL_TONS_TO_US_TONS

    def convert_to_pounds(self):
        return self.value * US_TONS_TO_POUNDS

    def convert_to_ounces(self):
        return self.value * US_TONS_TO_OUNCES
