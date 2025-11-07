import os.path

from src.input_function import input_function


def test_input_function():
    """
        Тесты функции input_function
    """
    assert input_function('cat requirements.txt') == 0
    assert input_function('cat ./requirements.txt') == 0
    assert input_function('cat .\\requirements.txt') == 0
    assert input_function('cat ' + os.path.abspath('requirements.txt')) == 0
    assert input_function('ls -l') == 0
    assert input_function('ls -l tests') == 0
