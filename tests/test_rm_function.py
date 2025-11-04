import os.path

from src.rm_function import rm


def test_rm_function():
    """
        Тесты с неправильными командами
    """
    assert rm('tests/test2.zip','-r')==0
    assert rm(os.path.abspath('.history'),'')==0