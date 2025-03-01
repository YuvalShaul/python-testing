"""
Module containing advanced calculator operations.
"""

import math
from calculator.utils.validators import validate_numeric


def power(base, exponent):
    """
    Raise base to the power of exponent.
    
    Args:
        base: The base number
        exponent: The exponent
        
    Returns:
        base raised to the power of exponent
        
    Raises:
        TypeError: If base or exponent is not a number
        ValueError: If attempting to raise a negative number to a fractional exponent
    """
    validate_numeric(base, exponent)
    
    # Handle special case: negative base with fractional exponent
    if base < 0 and not exponent.is_integer():
        raise ValueError("Cannot raise negative number to a fractional power")
        
    return math.pow(base, exponent)


def square_root(number):
    """
    Calculate the square root of a number.
    
    Args:
        number: The number to find the square root of
        
    Returns:
        The square root of the number
        
    Raises:
        TypeError: If number is not a number
        ValueError: If number is negative
    """
    validate_numeric(number)
    
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number")
        
    return math.sqrt(number)