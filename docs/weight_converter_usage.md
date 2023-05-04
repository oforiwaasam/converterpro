# ⛯ Weight Converter Usage

Below are some usage examples for this library:

```python3
>>> from converterpro import weight_converter
>>> my_gram = weight_converter.Gram(1.0)
>>> my_gram.convert_to_metric_tonnes()
0.000001
>>> val = weight_converter.Milligram(1.0)
>>> val.convert_to_grams()
0.001
>>> val = weight_converter.Kilogram(1.0)
>>> val.convert_to_milligrams()
1000000.0
>>> val = weight_converter.MetricTonnes(1.0)
>>> val.convert_to_kilograms()
1000.0
>>> val = weight_converter.ImperialTons(1.0)
>>> val.convert_to_us_tons()
1.12
>>> val = weight_converter.USTons(1.0)
>>> val.convert_to_pounds()
2000.0
>>> val = weight_converter.Pounds(1.0)
>>> val.convert_to_us_tons()
0.0005
>>> val = weight_converter.Ounces(1.0)
>>> val.convert_to_pounds()
0.0625
```
