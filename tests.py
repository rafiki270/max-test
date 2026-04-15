"""tests.py - tests for calculator."""

from calculator import calculate_average, process_numbers, divide, median, is_even, square

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
    with pytest.raises(ValueError):
        divide(10, 0)

def test_average_empty():
    import pytest
    with pytest.raises(ValueError):
        calculate_average([])

def test_process_numbers_empty():
    result = process_numbers([])
    assert result == {}

def test_median_odd_length():
    assert median([1, 3, 2]) == 2.0

def test_median_even_length():
    assert median([1, 2, 3, 4]) == 2.5

def test_median_empty():
    import pytest
    with pytest.raises(ValueError):
        median([])

def test_is_even_positive_even():
    assert is_even(4) is True

def test_is_even_positive_odd():
    assert is_even(7) is False

def test_is_even_zero():
    assert is_even(0) is True

def test_is_even_negative_even():
    assert is_even(-6) is True

def test_square_positive():
    assert square(5) == 25

def test_square_zero():
    assert square(0) == 0

def test_square_negative():
    assert square(-3) == 9