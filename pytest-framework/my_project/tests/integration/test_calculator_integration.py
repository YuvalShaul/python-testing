"""
Integration tests for the calculator package.
"""

import pytest
import calculator


class TestCalculatorIntegration:
    """Integration test cases for the calculator package."""
    
    def test_import_functions(self):
        """Test that all expected functions are imported and accessible."""
        # Basic operations
        assert callable(calculator.add)
        assert callable(calculator.subtract)
        assert callable(calculator.multiply)
        assert callable(calculator.divide)
        
        # Advanced operations
        assert callable(calculator.power)
        assert callable(calculator.square_root)
        
    def test_chained_operations(self):
        """Test functions can be chained together correctly."""
        # (5 + 3) * 2 = 16
        result = calculator.multiply(calculator.add(5, 3), 2)
        assert result == 16
        
        # √(25 - 9) = 4
        result = calculator.square_root(calculator.subtract(25, 9))
        assert result == 4
        
        # (10 / 2)^3 = 125
        result = calculator.power(calculator.divide(10, 2), 3)
        assert result == 125
        
    def test_complex_calculation(self):
        """Test a more complex calculation using multiple operations."""
        # ((5 * 4) + (10 / 2)) ^ 2 - √16 = 36 - 4 = 32
        step1 = calculator.multiply(5, 4)  # 20
        step2 = calculator.divide(10, 2)   # 5
        step3 = calculator.add(step1, step2)  # 25
        step4 = calculator.power(step3, 2)  # 625
        step5 = calculator.square_root(16)  # 4
        result = calculator.subtract(step4, step5)  # 621
        assert result == 621
        
    @pytest.mark.parametrize("operation,inputs,expected", [
        # (a + b) * c
        (lambda a, b, c: calculator.multiply(calculator.add(a, b), c),
         (2, 3, 4), 20),
        
        # (a - b) / c
        (lambda a, b, c: calculator.divide(calculator.subtract(a, b), c),
         (10, 4, 2), 3),
         
        # (a * b) ^ c
        (lambda a, b, c: calculator.power(calculator.multiply(a, b), c),
         (2, 3, 2), 36),
         
        # √(a + b)
        (lambda a, b: calculator.square_root(calculator.add(a, b)),
         (16, 9), 5),
    ])
    def test_combined_operations_parametrized(self, operation, inputs, expected):
        """Test various combined operations with parametrized inputs."""
        assert operation(*inputs) == pytest.approx(expected)
        
    def test_error_propagation(self):
        """Test that errors are properly propagated through chained operations."""
        # Try to calculate square root of (10 - 20), which is negative
        with pytest.raises(ValueError):
            calculator.square_root(calculator.subtract(10, 20))
            
        # Try to divide by the result of (5 - 5), which is zero
        with pytest.raises(ZeroDivisionError):
            calculator.divide(10, calculator.subtract(5, 5))
            
        # Try to raise a negative number to a fractional power
        with pytest.raises(ValueError):
            calculator.power(calculator.subtract(0, 5), 0.5)
            
        # Try with non-numeric inputs
        with pytest.raises(TypeError):
            calculator.add(calculator.add(5, 5), "string")