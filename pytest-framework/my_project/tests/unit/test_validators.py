"""
Unit tests for the validators module.
"""

import pytest
from calculator.utils.validators import validate_numeric


class TestValidateNumeric:
    """Test cases for the validate_numeric function."""
    
    def test_valid_integers(self):
        """Test that validation passes for integers."""
        # Should not raise any exception
        validate_numeric(1)
        validate_numeric(0)
        validate_numeric(-1)
        validate_numeric(1, 2, 3)
        
    def test_valid_floats(self):
        """Test that validation passes for floats."""
        # Should not raise any exception
        validate_numeric(1.0)
        validate_numeric(0.0)
        validate_numeric(-1.5)
        validate_numeric(1.5, 2.75, 3.25)
        
    def test_valid_complex(self):
        """Test that validation passes for complex numbers."""
        # Should not raise any exception
        validate_numeric(complex(1, 2))
        validate_numeric(complex(0, 0))
        validate_numeric(complex(-1, -1))
        
    def test_valid_mixed_types(self):
        """Test that validation passes for mixed numeric types."""
        # Should not raise any exception
        validate_numeric(1, 2.5, complex(3, 4))
        
    def test_invalid_strings(self):
        """Test that validation fails for strings."""
        with pytest.raises(TypeError):
            validate_numeric("string")
        with pytest.raises(TypeError):
            validate_numeric(1, "string")
        with pytest.raises(TypeError):
            validate_numeric(1, 2, "string")
            
    def test_invalid_none(self):
        """Test that validation fails for None."""
        with pytest.raises(TypeError):
            validate_numeric(None)
        with pytest.raises(TypeError):
            validate_numeric(1, None)
            
    def test_invalid_lists(self):
        """Test that validation fails for lists."""
        with pytest.raises(TypeError):
            validate_numeric([1, 2, 3])
        with pytest.raises(TypeError):
            validate_numeric(1, [2, 3])
            
    def test_invalid_dictionaries(self):
        """Test that validation fails for dictionaries."""
        with pytest.raises(TypeError):
            validate_numeric({"key": "value"})
        with pytest.raises(TypeError):
            validate_numeric(1, {"key": "value"})
            
    def test_invalid_tuples(self):
        """Test that validation fails for tuples."""
        with pytest.raises(TypeError):
            validate_numeric((1, 2))
        with pytest.raises(TypeError):
            validate_numeric(1, (2, 3))
            
    def test_empty_args(self):
        """Test that validation with no arguments doesn't raise exception."""
        # Should not raise any exception
        validate_numeric()
        
    @pytest.mark.parametrize("invalid_value", [
        "123",
        [1, 2, 3],
        {"key": "value"},
        (1, 2, 3),
        None,
        True,
        False,
    ])
    def test_invalid_values_parametrized(self, invalid_value):
        """Test validation fails for various non-numeric types."""
        with pytest.raises(TypeError):
            validate_numeric(invalid_value)
        with pytest.raises(TypeError):
            validate_numeric(1, invalid_value)