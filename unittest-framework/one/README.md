### Running tests - Simple Case One

- In this scenario, we have the code and tests in the same file
- this file is called "calculator.py", which could not be discovered, as it does not begin with **test**

#### Option 1 - Running the file directly
- The **calculator.py** file contains **unittest.main()** call, so if you just run it as a file it should run:
```
python calculator.py
```
- It will also work if we run it as a module:
```
python -m calculator
```

#### Option 2 - unittest discovery (renaming file)

- unittest offers a test discovery option
- For this to work, we need to rename out file to something that begins with **test**
- Example:
```
PS C:\one> ren .\calculator.py test_calculator.py
PS C:\one> python -m unittest discover
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
PS C:\one> 
```

#### Option 3 - unittest discovery (changing discovery pattern)

```
PS C:\one> python -m unittest discover -p calculator.py

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
PS C:\one> 
```