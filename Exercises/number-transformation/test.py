from numpy import arange
from hex_to_decimal import hex_to_decimal
from decimal_to_hex import decimal_to_hex
from binary_to_decimal import binary_to_decimal
from decimal_to_binary import decimal_to_binary
from octal_to_decimal import octal_to_decimal
from decimal_to_octal import decimal_to_octal

from binary_to_hex import binary_to_hex
from binary_to_octal import binary_to_octal

from unittest import main, TestCase
from random import random, randint


class TestFunctions(TestCase):
    def test_hex(self):
        for value in arange(0, 100, 0.001):
            value = random() * randint(0, 1000)
            hex_ = decimal_to_hex(value)
            number = hex_to_decimal(hex_)
            self.assertEqual(number, value)

    def test_binary(self):
        for value in arange(0, 100, 0.001):
            value = random() * randint(0, 1000)
            binary_ = decimal_to_binary(value)
            number = binary_to_decimal(binary_)
            self.assertEqual(number, value)

    def test_octal(self):
        for value in arange(0, 100, 0.001):
            value = random() * randint(0, 1000)
            octal_ = decimal_to_octal(value)
            number = octal_to_decimal(octal_)
            self.assertEqual(number, value)

    def test_binary_to_decimal(self):
        for value in arange(0, 100, 0.001):
            value = random() * randint(0, 1000)
            binary_ = decimal_to_binary(value)
            number = binary_to_decimal(binary_)
            self.assertEqual(number, value)

    def test_binary_to_hex(self):
        for value in arange(0, 100, 0.001):
            value = random() * randint(0, 1000)
            binary_ = decimal_to_binary(value)
            hex_ = binary_to_hex(binary_)
            number = hex_to_decimal(hex_)
            self.assertEqual(number, value)

    def test_binary_to_octal(self):
        for value in arange(0, 100, 0.001):
            value = random() * randint(0, 1000)
            binary_ = decimal_to_binary(value)
            octal_ = binary_to_octal(binary_)
            number = octal_to_decimal(octal_)
            self.assertEqual(number, value)


if __name__ == '__main__':
    main()
