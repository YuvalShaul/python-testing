"""
Validation utilities for calculator operations.
"""

import numbers


def validate_numeric(*args):
    """
    Validate that all arguments are numeric types.
    
    Args:
        *args: Variable number of arguments to validate
        
    Raises:
        TypeError: If any argument is not a number
    """
    for i, arg in enumerate(args):
        # Check for numbers but also explicitly reject booleans
        if not isinstance(arg, numbers.Number) or isinstance(arg, bool):
            raise TypeError(f"Argument {i+1} must be a number, got {type(arg).__name__}")