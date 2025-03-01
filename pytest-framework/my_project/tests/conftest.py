"""
Pytest configuration for the calculator tests.
"""

import pytest


@pytest.fixture
def sample_numbers():
    """Fixture providing a set of sample numbers for testing."""
    return {
        'integers': (5, 3),
        'floats': (10.5, 2.5),
        'negatives': (-8, -4),
        'zero': (0, 0),
        'mixed': (100, -25)
    }


@pytest.fixture
def non_numeric_values():
    """Fixture providing non-numeric values for testing validation."""
    return ["string", None, [1, 2, 3], {"key": "value"}, (1, 2)]