import pytest
from fun_except import CustomException
from calculator_implemented import CalculatorImp

calculator = CalculatorImp()

def test_addition_success():
    result = calculator
