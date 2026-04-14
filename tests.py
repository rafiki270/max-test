"""tests.py - tests for calculator."""

import pytest
from calculator import calculate_average, process_numbers, divide, safe_divide


def test_divide():
    assert divide(10, 2) == 5.0


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Division by zero"):
        divide(10, 0)


def test_safe_divide_by_zero():
    assert safe_divide(10, 0) is None


def test_average():
    result = calculate_average([1, 2, 3, 4, 5])
    assert result == 3.0


def test_average_empty_list():
    with pytest.raises(ValueError, match="Cannot calculate average of empty list"):
        calculate_average([])


def test_process_numbers():
    result = process_numbers([1, 2, 3])
    assert result["average"] == 2.0
    assert result["sum"] == 6
    assert result["count"] == 3
    assert result["max"] == 3
    assert result["min"] == 1


def test_process_numbers_empty():
    result = process_numbers([])
    assert result == {}
