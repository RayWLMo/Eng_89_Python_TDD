# Python Test Driven Development (TDD)
Test driven development is a technique used where a test is designed before any code is written. Code is then designed to pass the test and that code is refactored to improve efficiency, code simplicity etc.

![TDD Diagram](https://raw.githubusercontent.com/RayWLMo/Eng_89_Python_TDD/main/TDD_Diagram.png)
- Use `unittest` and `pytest` packages
- `pip install pytest` to install `pytest` package
- `python -m pytest` in terminal to see results
- `python -m unittest discover -v`

## Step 1 - Create a calc_test.py file
- Importing unittest and pytest as these are the dependencies to create our tests and run
```py
import unittest
import pytest
```
- Importing `SimpleCalc` from `simple_calc`
- It will say there's an error because there isn't a file called simple_calc
```py
from simple_calc import SimpleCalc
```
Writing simple tests
```py
class Calctest(unittest.TestCase):  # Creating a test class
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
```
## Step 2 - Creating a simple_calc.py file
Now that the test is created, code needs to be written to pass the test and refactored
- Here the class is defined, and the basic calculator functions are added
```py
class SimpleCalc:
    def add(self, num1, num2):
        return num1 + num2  # If the outcome is 5, the condition is True and the test would pass

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        return num1 / num2
```

