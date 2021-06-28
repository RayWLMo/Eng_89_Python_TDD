# Importing unittest and pytest as these are the dependencies to create our tests and run

import unittest
import pytest

from simple_calc import SimpleCalc


class Calctest(unittest.TestCase):
    calc = SimpleCalc()

    # Assertions to write our test cases
    # Using the basic calculator example to write the tests first

    def test_add(self):
        # Naming conventions are essential to have the test in the name of the method
        self.assertEqual(self.calc.add(3, 2), 5)  # if True, the test would pass

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(3, 2), 1)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 2), 6)

    def test_divide(self):
        self.assertEqual(self.calc.divide(4, 2), 2)
