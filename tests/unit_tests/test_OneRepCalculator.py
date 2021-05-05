# This script tests the OneRepCalculator model object
from models import OneRepCalculator
import pytest


# test to ensure model object can be instantiated
def test_instantiation():
    calculator = OneRepCalculator.OneRepCalculator()
    assert calculator is not None


# test to ensure calculation with valid data passes
def test_calculate_one_rep_max():
    calculator = OneRepCalculator.OneRepCalculator()
    actual = calculator.calculate_one_rep_max(255, 5)
    expected = 287
    assert actual == expected


# test to ensure calculation with numbers < 0 returns 0
def test_calculate_one_rep_max_with_invalid_numbers():
    calculator = OneRepCalculator.OneRepCalculator()
    actual = calculator.calculate_one_rep_max(0, -1000000)
    expected = 0
    assert actual == expected


# test failure with invalid parameters
def test_calculate_one_rep_max_with_invalid_parameters():
    calculator = OneRepCalculator.OneRepCalculator()
    with pytest.raises(TypeError):
        calculator.calculate_one_rep_max("bench-press", "is my favorite exercise")
