"""calculator.py - a simple calculator with intentional bugs."""

def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("division by zero")
    return a / b

def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if not numbers:
        raise ValueError("cannot calculate average of empty list")
    total = sum(numbers)
    count = len(numbers)
    return total / count

def safe_divide(a, b):
    """Safely divide a by b, returning None on division by zero."""
    if b == 0:
        return None
    return a / b

def process_numbers(numbers):
    """Process a list of numbers and return stats."""
    if not numbers:
        raise ValueError("cannot process empty list")
    avg = calculate_average(numbers)
    return {
        "average": avg,
        "sum": sum(numbers),
        "count": len(numbers),
        "max": max(numbers),  # BUG: max() on empty list crashes
        "min": min(numbers),  # BUG: min() on empty list crashes
    }
