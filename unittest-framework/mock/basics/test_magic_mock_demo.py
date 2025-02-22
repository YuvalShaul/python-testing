from unittest.mock import Mock
from unittest.mock import MagicMock

def magic_case_1():
    print('---------------1--------------')
    magic = MagicMock()
    print(type(magic))
    mock2 = magic.my_func()  # This is just a configuration,but now my_func exist in mock2
    print(type(magic))
    
    print(magic.my_func.called)  # True

def magic_case_2():
    print('---------------2--------------')
    magic = MagicMock()
    print(type(magic))
    
    magic.my_func()
    magic.my_func()
    print(magic.my_func.call_count)
    try:
        print(magic.my_func.assert_called_once())
    except AssertionError as e:
        print(e )

def magic_case_3():
    print('---------------3--------------')
    magic = MagicMock()
    magic.my_func.return_value = 5
    res = magic.my_func()
    print(type(res))


    print(len(mock2))

magic_case_1()
magic_case_2()