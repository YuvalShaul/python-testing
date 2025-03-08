###  Markers

- Note that there is a marker called "one" on several (5) tests methods.  
For example:
```
@pytest.mark.one
    def test_negative_exponent(self):
        """Test calculating powers with negative exponent."""
        assert power(2, -2) == 0.25
        assert power(10, -1) == 0.1
```
- This marker is registerd (see it in pytest.ini file)
- Try running:
```
 pytest -m one
 ```
 To run only those tests that are marked one
- Try running:
```
  pytest -m "not one"
```
To run the other tests.