"""
Unit tests for the advanced_operations module.
"""

import pytest
import math
from calculator.advanced_operations import power, square_root


class TestPower:
    """Test cases for the power function."""
    
    def test_integer_powers(self):
        """Test calculating integer powers."""
        assert power(2, 3) == 8
        assert power(5, 2) == 25
        assert power(10, 0) == 1
        assert power(1, 10) == 1
        
    def test_negative_base(self):
        """Test calculating powers with negative base."""
        assert power(-2, 2) == 4
        assert power(-2, 3) == -8
        assert power(-3, 2) == 9
        
    @pytest.mark.one
    def test_negative_exponent(self):
        """Test calculating powers with negative exponent."""
        assert power(2, -2) == 0.25
        assert power(10, -1) == 0.1

    @pytest.mark.one
    def test_fractional_exponent(self):
        """Test calculating powers with fractional exponent."""
        assert power(4, 0.5) == 2
        assert power(27, 1/3) == pytest.approx(3)
        assert power(16, 0.25) == 2
        
    def test_negative_base_fractional_exponent(self):
        """Test that negative base with fractional exponent raises ValueError."""
        with pytest.raises(ValueError):
            power(-4, 0.5)
        with pytest.raises(ValueError):
            power(-27, 1/3)
            
    def test_zero_base_negative_exponent(self):
        """Test that zero base with negative exponent raises ZeroDivisionError."""
        with pytest.raises(ZeroDivisionError):
            power(0, -1)
        with pytest.raises(ZeroDivisionError):
            power(0, -0.5)
            
    @pytest.mark.parametrize("base,exponent,expected", [
        (2, 3, 8),
        (3, 2, 9),
        (4, 0.5, 2),
        (1, 100, 1),
        (100, 0, 1),
        (2, -1, 0.5),
    ])
    def test_power_parametrized(self, base, exponent, expected):
        """Test power function with parametrized inputs."""
        assert power(base, exponent) == pytest.approx(expected)
        
    def test_power_non_numeric(self, non_numeric_values):
        """Test power with non-numeric values raises TypeError."""
        for value in non_numeric_values:
            with pytest.raises(TypeError):
                power(value, 2)
            with pytest.raises(TypeError):
                power(2, value)


class TestSquareRoot:
    """Test cases for the square_root function."""
    
    def test_perfect_squares(self):
        """Test square roots of perfect squares."""
        assert square_root(0) == 0
        assert square_root(1) == 1
        assert square_root(4) == 2
        assert square_root(9) == 3
        assert square_root(16) == 4
        assert square_root(25) == 5
        
    def test_non_perfect_squares(self):
        """Test square roots of non-perfect squares."""
        assert square_root(2) == pytest.approx(1.4142135623730951)
        assert square_root(3) == pytest.approx(1.7320508075688772)
        assert square_root(10) == pytest.approx(3.1622776601683795)
        
    def test_float_inputs(self):
        """Test square roots of floating point numbers."""
        assert square_root(0.25) == 0.5
        assert square_root(2.25) == 1.5
        assert square_root(0.01) == 0.1
        
    def test_negative_inputs(self):
        """Test that negative inputs raise ValueError."""
        with pytest.raises(ValueError):
            square_root(-1)
        with pytest.raises(ValueError):
            square_root(-0.5)
            
    @pytest.mark.parametrize("number,expected", [
        (0, 0),
        (1, 1),
        (4, 2),
        (9, 3),
        (2, 1.4142135623730951),
        (0.25, 0.5),
    ])
    def test_square_root_parametrized(self, number, expected):
        """Test square_root function with parametrized inputs."""
        assert square_root(number) == pytest.approx(expected)
        
    def test_square_root_non_numeric(self, non_numeric_values):
        """Test square_root with non-numeric values raises TypeError."""
        for value in non_numeric_values:
            with pytest.raises(TypeError):
                square_root(value)