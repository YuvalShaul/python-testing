### Running tests - Simple Case Two

- We split the file into 2 files:
  - calculator.py  (the tested code)
  - test_calculator.py (tests)
- Now:
  - The test imports the tested code
  - The tested code does not import unittest

#### Running the tests
- Running the tests file directly:
```
python .\test_calculator.py
```
- Running the tests file as a module:
```
python -m test_calculator
```
- Using unittest discovery:
```
python -m unittest discover
```