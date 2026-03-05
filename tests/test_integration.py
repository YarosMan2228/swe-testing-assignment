"""
Integration tests for Quick-Calc.

These tests simulate realistic user interaction sequences, verifying that
the Calculator's input layer and core logic work together correctly end-to-end.

Run with: pytest tests/test_integration.py -v
"""

from io import StringIO
import pytest
from unittest.mock import patch
from calculator import Calculator
from main import main


# --- Helper: simulate a sequence of CLI inputs and capture output ---

def run_cli(*inputs: str) -> str:
    """
    Run the main() CLI with the given sequence of user inputs and return
    the full captured stdout as a single string.
    """
    input_stream = "\n".join(inputs) + "\n"
    with patch("builtins.input", side_effect=input_stream.splitlines()):
        with patch("sys.stdout", new_callable=StringIO) as mock_out:
            try:
                main()
            except (StopIteration, EOFError):
                pass  # end of simulated input
            return mock_out.getvalue()


# --- Integration Test 1: Full arithmetic sequence ---

def test_full_addition_sequence():
    """
    Simulate: select Add -> enter 5 -> enter 3 -> quit.
    The output must contain 'Result: 8.0'.
    """
    output = run_cli("1", "5", "3", "6")
    assert "8.0" in output


def test_full_subtraction_sequence():
    """
    Simulate: select Subtract -> enter 10 -> enter 4 -> quit.
    The output must contain 'Result: 6.0'.
    """
    output = run_cli("2", "10", "4", "6")
    assert "6.0" in output


def test_full_multiplication_sequence():
    """
    Simulate: select Multiply -> enter 6 -> enter 7 -> quit.
    The output must contain 'Result: 42.0'.
    """
    output = run_cli("3", "6", "7", "6")
    assert "42.0" in output


def test_full_division_sequence():
    """
    Simulate: select Divide -> enter 8 -> enter 2 -> quit.
    The output must contain 'Result: 4.0'.
    """
    output = run_cli("4", "8", "2", "6")
    assert "4.0" in output


# --- Integration Test 2: Clear after a calculation ---

def test_clear_resets_display_after_calculation():
    """
    Simulate: Add 5+3, then press Clear.
    The output must show 'Cleared. Result: 0' after the clear action.
    """
    output = run_cli("1", "5", "3", "5", "6")
    assert "Cleared. Result: 0" in output


# --- Integration Test 3: Division by zero is handled gracefully ---

def test_division_by_zero_shows_error_message():
    """
    Simulate: select Divide -> enter 10 -> enter 0.
    The CLI must display an error message instead of crashing.
    """
    output = run_cli("4", "10", "0", "6")
    assert "Error" in output or "Cannot divide by zero" in output
