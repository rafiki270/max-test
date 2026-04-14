"""tests.py - tests for calculator."""

from calculator import calculate_average, process_numbers, divide

def test_average():
    result = calculate_average([1, 2, 3, 4, 5])
    assert result == 3.0

def test_process_numbers():
    result = process_numbers([1, 2, 3])
    assert result["average"] == 2.0
    assert result["sum"] == 6
    assert result["count"] == 3

def test_divide():
    assert divide(10, 2) == 5.0

def test_divide_by_zero():
    import pytest
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

def test_average_empty_list():
    import pytest
    with pytest.raises(ValueError):
        calculate_average([])
