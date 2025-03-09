"""
Pytest configuration for the calculator tests.
"""

import pytest
import time


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



# Register the 'slow' marker
def pytest_configure(config):
    config.addinivalue_line("markers", "slow: marks tests that take a long time")

# Do something before tests with the 'slow' marker
def pytest_runtest_setup(item):
    # Check if this test has the 'slow' marker
    slow_marker = item.get_closest_marker("slow")
    if slow_marker:
        print(f"Setting up for slow test: {item.name}")
        # Store start time for tests with 'slow' marker
        item._start_time = time.time()

# Do something after tests with the 'slow' marker
def pytest_runtest_teardown(item, nextitem):
    # Check if this test has the 'slow' marker
    slow_marker = item.get_closest_marker("slow")
    if slow_marker and hasattr(item, '_start_time'):
        duration = time.time() - item._start_time
        print(f"\nSlow test {item.name} took {duration:.2f} seconds")