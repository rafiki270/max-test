"""calculator.py - a simple calculator with intentional bugs."""

def divide(a, b):
    """Divide a by b."""
    return a / b  # BUG: no check for division by zero

def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    total = sum(numbers)
    count = len(numbers)
    return total / count  # BUG: crashes if list is empty

def safe_divide(a, b):
    """Safely divide a by b, returning None on division by zero."""
    if b == 0:
        return None
    return a / b

def process_numbers(numbers):
    """Process a list of numbers and return stats."""
    if not numbers:
        return {}
    avg = calculate_average(numbers)
    return {
        "average": avg,
        "sum": sum(numbers),
        "count": len(numbers),
        "max": max(numbers),  # BUG: max() on empty list crashes
        "min": min(numbers),  # BUG: min() on empty list crashes
    }
