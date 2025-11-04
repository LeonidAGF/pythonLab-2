import os

from src.cp_function import cp
from src.rm_function import rm


def test_cp_function():
    """
        Тесты для еоманды cp
    """
    assert cp(os.path.abspath('tests'), 'test1', '') == 0
    rm('test1', '')
    assert cp('tests', 'test1', '-r') == 0
    rm('test1', '-r')
    assert cp('requirements.txt', 'test1', '') == 0
    rm('test1', '')
