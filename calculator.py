"""calculator.py - a simple calculator with intentional bugs."""

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b

def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    total = sum(numbers)
    count = len(numbers)
    return total / count

def safe_divide(a, b):
    """Safely divide a by b, returning None on division by zero."""
    if b == 0:
        return None
    return a / b

def median(numbers):
    """Calculate the median of a list of integers."""
    if not numbers:
        raise ValueError("Cannot calculate median of empty list")
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    return float(sorted_nums[mid])

def is_even(n):
    """Return True if n is even, False if odd."""
    return n % 2 == 0

def square(n):
    """Return the value multiplied by itself."""
    return n * n

def fifth_power(value):
    """Return the value multiplied by itself five times."""
    return value * value * value * value * value

def process_numbers(numbers):
    """Process a list of numbers and return stats."""
    if not numbers:
        return {}
    avg = calculate_average(numbers)
    return {
        "average": avg,
        "sum": sum(numbers),
        "count": len(numbers),
        "max": max(numbers),
        "min": min(numbers),
    }
