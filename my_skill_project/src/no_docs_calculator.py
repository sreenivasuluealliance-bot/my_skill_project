"""
Calculator module providing basic arithmetic operations.

This module contains functions for performing fundamental mathematical operations
including addition, subtraction, multiplication, division, percentage calculation,
and exponentiation.
"""

def add(a, b):
    """Add two numbers.

    Args:
        a: First number (int or float)
        b: Second number (int or float)

    Returns:
        The sum of a and b
    """
    return a + b

def subtract(a, b):
    """Subtract one number from another.

    Args:
        a: Number to subtract from (int or float)
        b: Number to subtract (int or float)

    Returns:
        The difference (a - b)
    """
    return a - b

def multiply(a, b):
    """Multiply two numbers.

    Args:
        a: First number (int or float)
        b: Second number (int or float)

    Returns:
        The product of a and b
    """
    return a * b

def divide(a, b):
    """Divide one number by another.

    Args:
        a: Numerator (int or float)
        b: Denominator (int or float)

    Returns:
        The quotient (a / b)

    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def get_percentage(value, total):
    """Calculate what percentage a value is of a total.

    Args:
        value: The value to calculate percentage for (int or float)
        total: The total amount (int or float)

    Returns:
        The percentage as a float (0-100)

    Raises:
        ValueError: If total is zero
    """
    if total == 0:
        raise ValueError("Total cannot be zero!")
    return (value / total) * 100

def power(base, exponent):
    """Raise a base number to a given exponent.

    Args:
        base: The base number (int or float)
        exponent: The exponent (int or float)

    Returns:
        The result of base raised to the power of exponent
    """
    return base ** exponent