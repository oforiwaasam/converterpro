THOUSAND = 1e3
MILLION = 1e6
BILLION = 1e9
TRILLION = 1e12

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

POUNDS_TO_OUNCES = 16


# METRIC SYSTEM OF MEASUREMENTS
class Gram:
    """
    The Gram class converts from grams to other units.

    """

    def __init__(self, value):
        """
        Constructs all the necessary attributes for the Gram object.

        Parameters
        ----------
            value : float
                value to be converted from Grams

        """

        self.value = value

    def convert_to_grams(self):
        """
        Converts value to grams

        Returns:
            float: The new value in grams
        """
        return self.value

    def convert_to_milligrams(self):
        """
        Converts value to milligrams

        Returns:
            float: The new value in milligrams
        """
        return self.value * THOUSAND

    def convert_to_kilograms(self):
        """
        Converts value to kilograms

        Returns:
            float: The new value in kilograms
        """
        return self.value / THOUSAND

    def convert_to_metric_tonnes(self):
        """
        Converts value to metric tonnes

        Returns:
            float: The new value in metric tonnes
        """
        return self.value / MILLION

    def convert_to_imperial_tons(self):
        """
        Converts value to imperial tons

        Returns:
            float: The new value in imperial tons
        """
        return self.value / GRAMS_TO_IMPERIAL_TONS

    def convert_to_us_tons(self):
        """
        Converts value to us tons

        Returns:
            float: The new value in us tons
        """
        return self.value / GRAMS_TO_US_TONS

    def convert_to_pounds(self):
        """
        Converts value to pounds

        Returns:
            float: The new value in pounds
        """
        return self.value / GRAMS_TO_POUNDS

    def convert_to_ounces(self):
        """
        Converts value to ounces

        Returns:
            float: The new value in ounces
        """
        return self.value / GRAMS_TO_OUNCES


class Milligram:
    """
    The Milligram class converts from milligrams to other units.

    Attributes
    ----------
    value : float
        the value in Milligrams that is to be converted.

    """

    def __init__(self, value):
        """
        Constructs all the necessary attributes for the Milligram object.

        Parameters
        ----------
            value : float
                value to be converted from Milligrams

        """

        self.value = value

    def convert_to_grams(self):
        """
        Converts value to grams

        Returns:
            float: The new value in grams
        """
        return self.value / THOUSAND

    def convert_to_milligrams(self):
        """
        Converts value to milligrams

        Returns:
            float: The new value in milligrams
        """
        return self.value

    def convert_to_kilograms(self):
        """
        Converts value to kilograms

        Returns:
            float: The new value in kilograms
        """
        return self.value / MILLION

    def convert_to_metric_tonnes(self):
        """
        Converts value to metric tonnes

        Returns:
            float: The new value in metric tonnes
        """
        return self.value / BILLION

    def convert_to_imperial_tons(self):
        """
        Converts value to imperial tons

        Returns:
            float: The new value in imperial tons
        """
        return self.value / MILLIGRAMS_TO_IMPERIAL_TONS

    def convert_to_us_tons(self):
        """
        Converts value to us tons

        Returns:
            float: The new value in us tons
        """
        return self.value / MILLIGRAMS_TO_US_TONS

    def convert_to_pounds(self):
        """
        Converts value to pounds

        Returns:
            float: The new value in pounds
        """
        return self.value / MILLIGRAMS_TO_POUNDS

    def convert_to_ounces(self):
        """
        Converts value to ounces

        Returns:
            float: The new value in ounces
        """
        return self.value / MILLIGRAMS_TO_OUNCES


class Kilogram:
    """
    The Kilogram class converts from kilograms to other units.

    Attributes
    ----------
    value : float
        the value in Kilograms that is to be converted.

    """

    def __init__(self, value):
        """
        Constructs all the necessary attributes for the Kilogram object.

        Parameters
        ----------
            value : float
                value to be converted from Kilograms

        """

        self.value = value

    def convert_to_grams(self):
        """
        Converts value to grams

        Returns:
            float: The new value in grams
        """
        return self.value * THOUSAND

    def convert_to_milligrams(self):
        """
        Converts value to milligrams

        Returns:
            float: The new value in milligrams
        """
        return self.value * MILLION

    def convert_to_kilograms(self):
        """
        Converts value to kilograms

        Returns:
            float: The new value in kilograms
        """
        return self.value

    def convert_to_metric_tonnes(self):
        """
        Converts value to metric tonnes

        Returns:
            float: The new value in metric tonnes
        """
        return self.value / THOUSAND

    def convert_to_imperial_tons(self):
        """
        Converts value to imperial tons

        Returns:
            float: The new value in imperial tons
        """
        return self.value / KILOGRAMS_TO_IMPERIAL_TONS

    def convert_to_us_tons(self):
        """
        Converts value to us tons

        Returns:
            float: The new value in us tons
        """
        return self.value / KILOGRAMS_TO_US_TONS

    def convert_to_pounds(self):
        """
        Converts value to pounds

        Returns:
            float: The new value in pounds
        """
        return self.value * KILOGRAMS_TO_POUNDS

    def convert_to_ounces(self):
        """
        Converts value to ounces

        Returns:
            float: The new value in ounces
        """
        return self.value * KILOGRAMS_TO_OUNCES


class MetricTonnes:
    """
    The MetricTonnes class converts from Metric tonnes to other units.

    Attributes
    ----------
    value : float
        the value in MetricTonnes that is to be converted.

    """

    def __init__(self, value):
        """
        Constructs all the necessary attributes for the MetricTonnes object.

        Parameters
        ----------
            value : float
                value to be converted from MetricTonnes

        """

        self.value = value

    def convert_to_grams(self):
        """
        Converts value to grams

        Returns:
            float: The new value in grams
        """
        return self.value * MILLION

    def convert_to_milligrams(self):
        """
        Converts value to milligrams

        Returns:
            float: The new value in milligrams
        """
        return self.value * BILLION

    def convert_to_kilograms(self):
        """
        Converts value to kilograms

        Returns:
            float: The new value in kilograms
        """
        return self.value * THOUSAND

    def convert_to_metric_tonnes(self):
        """
        Converts value to metric tonnes

        Returns:
            float: The new value in metric tonnes
        """
        return self.value

    def convert_to_imperial_tons(self):
        """
        Converts value to imperial tons

        Returns:
            float: The new value in imperial tons
        """
        return self.value / METRIC_TONNES_TO_IMPERIAL_TONS

    def convert_to_us_tons(self):
        """
        Converts value to us tons

        Returns:
            float: The new value in us tons
        """
        return self.value * METRIC_TONNES_TO_US_TONS

    def convert_to_pounds(self):
        """
        Converts value to pounds

        Returns:
            float: The new value in pounds
        """
        return self.value * METRIC_TONNES_TO_POUNDS

    def convert_to_ounces(self):
        """
        Converts value to ounces

        Returns:
            float: The new value in ounces
        """
        return self.value * METRIC_TONNES_TO_OUNCES


# UK TONS / IMPERIAL TONS
class ImperialTons:
    """
    The ImperialTons class converts from imperial tons to other units.

    Attributes
    ----------
    value : float
        the value in ImperialTons that is to be converted.

    """

    def __init__(self, value):
        """
        Constructs all the necessary attributes for the ImperialTons object.

        Parameters
        ----------
            value : float
                value to be converted from ImperialTons

        """

        self.value = value

    def convert_to_grams(self):
        """
        Converts value to grams

        Returns:
            float: The new value in grams
        """
        return self.value * GRAMS_TO_IMPERIAL_TONS

    def convert_to_milligrams(self):
        """
        Converts value to milligrams

        Returns:
            float: The new value in milligrams
        """
        return self.value * MILLIGRAMS_TO_IMPERIAL_TONS

    def convert_to_kilograms(self):
        """
        Converts value to kilograms

        Returns:
            float: The new value in kilograms
        """
        return self.value * KILOGRAMS_TO_IMPERIAL_TONS

    def convert_to_metric_tonnes(self):
        """
        Converts value to metric tonnes

        Returns:
            float: The new value in metric tonnes
        """
        return self.value * METRIC_TONNES_TO_IMPERIAL_TONS

    def convert_to_imperial_tons(self):
        """
        Converts value to imperial tons

        Returns:
            float: The new value in imperial tons
        """
        return self.value

    def convert_to_us_tons(self):
        """
        Converts value to us tons

        Returns:
            float: The new value in us tons
        """
        return self.value * IMPERIAL_TONS_TO_US_TONS

    def convert_to_pounds(self):
        """
        Converts value to pounds

        Returns:
            float: The new value in pounds
        """
        return self.value * IMPERIAL_TONS_TO_POUNDS

    def convert_to_ounces(self):
        """
        Converts value to ounces

        Returns:
            float: The new value in ounces
        """
        return self.value * IMPERIAL_TONS_TO_OUNCES


# US TONS
class USTons:
    """
    The USTons class converts from US Tons to other units.

    Attributes
    ----------
    value : float
        the value in USTons that is to be converted.

    """

    def __init__(self, value):
        """
        Constructs all the necessary attributes for the USTons object.

        Parameters
        ----------
            value : float
                value to be converted from USTons

        """

        self.value = value

    def convert_to_grams(self):
        """
        Converts value to grams

        Returns:
            float: The new value in grams
        """
        return self.value * GRAMS_TO_US_TONS

    def convert_to_milligrams(self):
        """
        Converts value to milligrams

        Returns:
            float: The new value in milligrams
        """
        return self.value * MILLIGRAMS_TO_US_TONS

    def convert_to_kilograms(self):
        """
        Converts value to kilograms

        Returns:
            float: The new value in kilograms
        """
        return self.value * KILOGRAMS_TO_US_TONS

    def convert_to_metric_tonnes(self):
        """
        Converts value to metric tonnes

        Returns:
            float: The new value in metric tonnes
        """
        return self.value / METRIC_TONNES_TO_US_TONS

    def convert_to_imperial_tons(self):
        """
        Converts value to imperial tons

        Returns:
            float: The new value in imperial tons
        """
        return self.value / IMPERIAL_TONS_TO_US_TONS

    def convert_to_us_tons(self):
        """
        Converts value to us tons

        Returns:
            float: The new value in us tons
        """
        return self.value

    def convert_to_pounds(self):
        """
        Converts value to pounds

        Returns:
            float: The new value in pounds
        """
        return self.value * US_TONS_TO_POUNDS

    def convert_to_ounces(self):
        """
        Converts value to ounces

        Returns:
            float: The new value in ounces
        """
        return self.value * US_TONS_TO_OUNCES


class Pounds:
    """
    The Pounds class converts from pounds to other units.

    Attributes
    ----------
    value : float
        the value in Pounds that is to be converted.

    """

    def __init__(self, value):
        """
        Constructs all the necessary attributes for the Pound object.

        Parameters
        ----------
            value : float
                value to be converted from Pounds

        """

        self.value = value

    def convert_to_grams(self):
        """
        Converts value to grams

        Returns:
            float: The new value in grams
        """
        return self.value * GRAMS_TO_POUNDS

    def convert_to_milligrams(self):
        """
        Converts value to milligrams

        Returns:
            float: The new value in milligrams
        """
        return self.value * MILLIGRAMS_TO_POUNDS

    def convert_to_kilograms(self):
        """
        Converts value to kilograms

        Returns:
            float: The new value in kilograms
        """
        return self.value / KILOGRAMS_TO_POUNDS

    def convert_to_metric_tonnes(self):
        """
        Converts value to metric tonnes

        Returns:
            float: The new value in metric tonnes
        """
        return self.value / METRIC_TONNES_TO_POUNDS

    def convert_to_imperial_tons(self):
        """
        Converts value to imperial tons

        Returns:
            float: The new value in imperial tons
        """
        return self.value / IMPERIAL_TONS_TO_POUNDS

    def convert_to_us_tons(self):
        """
        Converts value to us tons

        Returns:
            float: The new value in us tons
        """
        return self.value / US_TONS_TO_POUNDS

    def convert_to_pounds(self):
        """
        Converts value to pounds

        Returns:
            float: The new value in pounds
        """
        return self.value

    def convert_to_ounces(self):
        """
        Converts value to ounces

        Returns:
            float: The new value in ounces
        """
        return self.value * POUNDS_TO_OUNCES


class Ounces:
    """
    The Ounces class converts from ounces to other units.

    Attributes
    ----------
    value : float
        the value in Ounces that is to be converted.

    """

    def __init__(self, value: float = 1.0):
        """
        Constructs all the necessary attributes for the Ounce object.

        Parameters
        ----------
            value : float
                value to be converted from Ounces

        """

        self.value = value

    def convert_to_grams(self):
        """
        Converts value to grams

        Returns:
            float: The new value in grams
        """
        return self.value * GRAMS_TO_OUNCES

    def convert_to_milligrams(self):
        """
        Converts value to milligrams

        Returns:
            float: The new value in milligrams
        """
        return self.value * MILLIGRAMS_TO_OUNCES

    def convert_to_kilograms(self):
        """
        Converts value to kilograms

        Returns:
            float: The new value in kilograms
        """
        return self.value / KILOGRAMS_TO_OUNCES

    def convert_to_metric_tonnes(self):
        """
        Converts value to metric tonnes

        Returns:
            float: The new value in metric tonnes
        """
        return self.value / METRIC_TONNES_TO_OUNCES

    def convert_to_imperial_tons(self):
        """
        Converts value to imperial tons

        Returns:
            float: The new value in imperial tons
        """
        return self.value / IMPERIAL_TONS_TO_OUNCES

    def convert_to_us_tons(self):
        """
        Converts value to us tons

        Returns:
            float: The new value in us tons
        """
        return self.value / US_TONS_TO_OUNCES

    def convert_to_pounds(self):
        """
        Converts value to pounds

        Returns:
            float: The new value in pounds
        """
        return self.value / POUNDS_TO_OUNCES

    def convert_to_ounces(self):
        """
        Converts value to ounces

        Returns:
            float: The new value in ounces
        """
        return self.value
