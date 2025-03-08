"""
Unit tests for the basic_operations module.
"""

import pytest
from calculator.basic_operations import add, subtract, multiply, divide


class TestAdd:
    """Test cases for the add function."""
    
    def test_add_integers(self, sample_numbers):
        """Test adding two integers."""
        a, b = sample_numbers['integers']
        assert add(a, b) == 8
        
    def test_add_floats(self, sample_numbers):
        """Test adding two floats."""
        a, b = sample_numbers['floats']
        assert add(a, b) == 13.0
        
    @pytest.mark.one
    def test_add_negatives(self, sample_numbers):
        """Test adding two negative numbers."""
        a, b = sample_numbers['negatives']
        assert add(a, b) == -12
        
    @pytest.mark.one
    def test_add_mixed(self, sample_numbers):
        """Test adding a positive and negative number."""
        a, b = sample_numbers['mixed']
        assert add(a, b) == 75
        
    def test_add_zeros(self, sample_numbers):
        """Test adding zeros."""
        a, b = sample_numbers['zero']
        assert add(a, b) == 0
        
    def test_add_non_numeric(self, non_numeric_values):
        """Test adding non-numeric values raises TypeError."""
        for value in non_numeric_values:
            with pytest.raises(TypeError):
                add(value, 5)
            with pytest.raises(TypeError):
                add(5, value)


class TestSubtract:
    """Test cases for the subtract function."""
    
    def test_subtract_integers(self, sample_numbers):
        """Test subtracting two integers."""
        a, b = sample_numbers['integers']
        assert subtract(a, b) == 2
        
    def test_subtract_floats(self, sample_numbers):
        """Test subtracting two floats."""
        a, b = sample_numbers['floats']
        assert subtract(a, b) == 8.0
        
    def test_subtract_negatives(self, sample_numbers):
        """Test subtracting two negative numbers."""
        a, b = sample_numbers['negatives']
        assert subtract(a, b) == -4
        
    def test_subtract_mixed(self, sample_numbers):
        """Test subtracting a negative from a positive number."""
        a, b = sample_numbers['mixed']
        assert subtract(a, b) == 125
        
    def test_subtract_zeros(self, sample_numbers):
        """Test subtracting zeros."""
        a, b = sample_numbers['zero']
        assert subtract(a, b) == 0
        
    def test_subtract_non_numeric(self, non_numeric_values):
        """Test subtracting non-numeric values raises TypeError."""
        for value in non_numeric_values:
            with pytest.raises(TypeError):
                subtract(value, 5)
            with pytest.raises(TypeError):
                subtract(5, value)


class TestMultiply:
    """Test cases for the multiply function."""
    
    def test_multiply_integers(self, sample_numbers):
        """Test multiplying two integers."""
        a, b = sample_numbers['integers']
        assert multiply(a, b) == 15
        
    def test_multiply_floats(self, sample_numbers):
        """Test multiplying two floats."""
        a, b = sample_numbers['floats']
        assert multiply(a, b) == 26.25
        
    def test_multiply_negatives(self, sample_numbers):
        """Test multiplying two negative numbers."""
        a, b = sample_numbers['negatives']
        assert multiply(a, b) == 32
        
    def test_multiply_mixed(self, sample_numbers):
        """Test multiplying a positive and negative number."""
        a, b = sample_numbers['mixed']
        assert multiply(a, b) == -2500
        
    def test_multiply_by_zero(self, sample_numbers):
        """Test multiplying by zero."""
        a, _ = sample_numbers['integers']
        assert multiply(a, 0) == 0
        assert multiply(0, a) == 0
        
    def test_multiply_non_numeric(self, non_numeric_values):
        """Test multiplying non-numeric values raises TypeError."""
        for value in non_numeric_values:
            with pytest.raises(TypeError):
                multiply(value, 5)
            with pytest.raises(TypeError):
                multiply(5, value)


class TestDivide:
    """Test cases for the divide function."""
    
    def test_divide_integers(self, sample_numbers):
        """Test dividing two integers."""
        a, b = sample_numbers['integers']
        assert divide(a, b) == pytest.approx(1.6666666666666667)
        
    def test_divide_floats(self, sample_numbers):
        """Test dividing two floats."""
        a, b = sample_numbers['floats']
        assert divide(a, b) == 4.2
        
    def test_divide_negatives(self, sample_numbers):
        """Test dividing two negative numbers."""
        a, b = sample_numbers['negatives']
        assert divide(a, b) == 2.0
        
    def test_divide_mixed(self, sample_numbers):
        """Test dividing a positive by a negative number."""
        a, b = sample_numbers['mixed']
        assert divide(a, b) == -4.0
        
    def test_divide_by_zero(self, sample_numbers):
        """Test dividing by zero raises ZeroDivisionError."""
        a, _ = sample_numbers['integers']
        with pytest.raises(ZeroDivisionError):
            divide(a, 0)
            
    def test_divide_zero_by_number(self, sample_numbers):
        """Test dividing zero by a number."""
        _, b = sample_numbers['integers']
        assert divide(0, b) == 0
        
    def test_divide_non_numeric(self, non_numeric_values):
        """Test dividing non-numeric values raises TypeError."""
        for value in non_numeric_values:
            with pytest.raises(TypeError):
                divide(value, 5)
            with pytest.raises(TypeError):
                divide(5, value)