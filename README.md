# ConverterPro

A python library to convert units and currencies

![Hex.pm](https://img.shields.io/hexpm/l/apa?style=flat&color=brightgreen)
![GitHub issues](https://img.shields.io/github/issues/oforiwaasam/converterpro)
[![Build Status](https://img.shields.io/github/actions/workflow/status/oforiwaasam/converterpro/build.yml)](https://github.com/oforiwaasam/converterpro/actions/workflows/build.yml)
[![Coverage Status](https://coveralls.io/repos/github/oforiwaasam/converterpro/badge.svg?branch=main)](https://coveralls.io/github/oforiwaasam/converterpro?branch=main)
[![black](https://img.shields.io/badge/code%20style-black-000000)](https://github.com/psf/black)
[![poetry](https://img.shields.io/badge/packaging-poetry-008adf)](https://python-poetry.org/)
[![PyPI](https://img.shields.io/pypi/v/converterpro)](https://pypi.org/project/converterpro/)
[![Deployment](https://img.shields.io/github/deployments/oforiwaasam/converterpro/github-pages?label=GitHub&nbsp;Pages)](https://oforiwaasam.github.io/converterpro)

## 🔭 Overview

This python library will allow developers to easily incorporate conversions into their programs without having to write all the logic for it. The library currently has the following functionalities:

## 📝 Features

+ Weight conversion between Metric, Imperial and US Systems of Measurement
  + Grams
  + Milligrams
  + Kilograms

## 🛠️ Installation

**converterpro** can be found on PyPi and hence can be installed with `pip`:

```bash
pip install converterpro
```

## ⛯ Usage

```python3
>>> from converterpro import weight_converter
>>> my_gram = weight_converter.Gram(1.0)
>>> my_gram.convert_to_kilograms()
0.001
```

## 📝 Details

This library project is a pure python project using modern tooling. It uses a `Makefile` as a command registry, with the following commands:

+ `make`: list available commands
+ `make install`: install and build this library and its dependencies using `poetry`
+ `make lint`: perform static analysis of this library with `ruff` and `black`
+ `make format`: autoformat this library using `black` and `ruff`
+ `make test`: run automated tests with `pytest`
+ `make coverage`: run automated tests with `pytest` and collect coverage information

## 👩🏾‍💻👨🏾‍💻 Contributing

Please see [CONTRIBUTING](CONTRIBUTING.md) for more information.

## 🪪 License

This software is licensed under the Apache 2.0 license. Please see [LICENSE](LICENSE) for more information.

## 🙎🏾‍ Author

Main Maintainer: Lily Sam
