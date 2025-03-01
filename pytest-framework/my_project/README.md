# Calculator Package

A simple calculator package with basic and advanced mathematical operations.

## Features

- Basic operations: add, subtract, multiply, divide
- Advanced operations: power, square root
- Input validation
- Comprehensive test suite

## Installation

```bash
# Install in development mode
pip install -e .

# For regular installation
pip install .
```

## Usage

```python
from calculator import add, subtract, multiply, divide, power, square_root

# Basic operations
add(5, 3)  # 8
subtract(10, 4)  # 6
multiply(3, 7)  # 21
divide(15, 3)  # 5.0

# Advanced operations
power(2, 3)  # 8
square_root(16)  # 4.0
```

## Development

### Running Tests

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=calculator

# Run specific test file
pytest tests/unit/test_basic_operations.py
```

## Project Structure

This project follows the recommended src-layout pattern:

```
my_calculator/
├── pyproject.toml
├── README.md
├── src/
│   └── calculator/
│       ├── __init__.py
│       ├── basic_operations.py
│       ├── advanced_operations.py
│       └── utils/
│           ├── __init__.py
│           └── validators.py
└── tests/
    ├── conftest.py
    ├── __init__.py
    ├── pytest.ini
    ├── unit/
    │   ├── __init__.py
    │   ├── test_basic_operations.py
    │   ├── test_advanced_operations.py
    │   └── test_validators.py
    └── integration/
        ├── __init__.py
        └── test_calculator_integration.py
```

## License

MIT