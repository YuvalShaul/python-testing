"""
Module containing basic calculator operations.
"""

from calculator.utils.validators import validate_numeric


def add(a, b):
    """
    Add two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The sum of a and b
        
    Raises:
        TypeError: If a or b is not a number
    """
    validate_numeric(a, b)
    return a + b


def subtract(a, b):
    """
    Subtract b from a.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The difference (a - b)
        
    Raises:
        TypeError: If a or b is not a number
    """
    validate_numeric(a, b)
    return a - b


def multiply(a, b):
    """
    Multiply two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The product of a and b
        
    Raises:
        TypeError: If a or b is not a number
    """
    validate_numeric(a, b)
    return a * b


def divide(a, b):
    """
    Divide a by b.
    
    Args:
        a: Numerator
        b: Denominator
        
    Returns:
        The quotient of a divided by b
        
    Raises:
        TypeError: If a or b is not a number
        ZeroDivisionError: If b is zero
    """
    validate_numeric(a, b)
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b