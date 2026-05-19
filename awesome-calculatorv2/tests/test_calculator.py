"""
Тесты для калькулятора.
"""

import pytest
from awesome_calculator import Calculator, greet


def test_add():
    assert Calculator.add(2, 3) == 5
    assert Calculator.add(-1, 1) == 0
    assert Calculator.add(0, 0) == 0


def test_subtract():
    assert Calculator.subtract(5, 3) == 2
    assert Calculator.subtract(0, 5) == -5
    assert Calculator.subtract(10, 10) == 0


def test_multiply():
    assert Calculator.multiply(3, 4) == 12
    assert Calculator.multiply(-2, 3) == -6
    assert Calculator.multiply(0, 100) == 0


def test_divide():
    assert Calculator.divide(10, 2) == 5
    assert Calculator.divide(7, 2) == 3.5
    assert Calculator.divide(-10, 2) == -5


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Деление на ноль невозможно"):
        Calculator.divide(10, 0)


def test_greet():
    result = greet()
    assert "Hello" in result
    assert "v2" in result
    assert "Ratovskiy" in result
