"""
Unit tests for the Quick-Calc Calculator class.

Tests are isolated to individual methods of the Calculator class.
Run with: pytest tests/test_unit.py -v
"""

import pytest
from calculator import Calculator


@pytest.fixture
def calc():
    """Return a fresh Calculator instance for each test."""
    return Calculator()


# --- Addition ---

def test_add_two_positive_integers(calc):
    """5 + 3 should equal 8."""
    assert calc.add(5, 3) == 8


def test_add_negative_numbers(calc):
    """Adding two negatives should produce a more negative result."""
    assert calc.add(-4, -6) == -10


def test_add_positive_and_negative(calc):
    """A positive and a negative that partially cancel."""
    assert calc.add(10, -3) == 7


# --- Subtraction ---

def test_subtract_basic(calc):
    """10 - 4 should equal 6."""
    assert calc.subtract(10, 4) == 6


def test_subtract_producing_negative_result(calc):
    """Subtracting a larger number from a smaller one yields a negative."""
    assert calc.subtract(3, 10) == -7


# --- Multiplication ---

def test_multiply_two_positive_integers(calc):
    """6 * 7 should equal 42."""
    assert calc.multiply(6, 7) == 42


def test_multiply_by_zero(calc):
    """Any number multiplied by zero is zero."""
    assert calc.multiply(99, 0) == 0


def test_multiply_decimal_numbers(calc):
    """Multiplying decimals should be accurate to floating-point precision."""
    assert calc.multiply(2.5, 4.0) == pytest.approx(10.0)


# --- Division ---

def test_divide_basic(calc):
    """8 / 2 should equal 4."""
    assert calc.divide(8, 2) == 4


def test_divide_produces_decimal(calc):
    """7 / 2 should equal 3.5."""
    assert calc.divide(7, 2) == pytest.approx(3.5)


# --- Edge Cases ---

def test_divide_by_zero_raises_error(calc):
    """Dividing by zero must raise a ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(10, 0)


def test_add_very_large_numbers(calc):
    """Adding very large numbers should not overflow or lose precision."""
    assert calc.add(1e15, 2e15) == pytest.approx(3e15)


def test_subtract_decimal_numbers(calc):
    """Decimal subtraction should be accurate to floating-point precision."""
    assert calc.subtract(5.5, 2.2) == pytest.approx(3.3)


# --- Clear ---

def test_clear_resets_result_to_zero(calc):
    """After performing an operation, clear() should reset result to 0."""
    calc.add(5, 3)
    assert calc.result == 8
    calc.clear()
    assert calc.result == 0


def test_clear_returns_zero(calc):
    """clear() should explicitly return 0."""
    calc.multiply(9, 9)
    returned = calc.clear()
    assert returned == 0
