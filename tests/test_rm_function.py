import os.path

from src.rm_function import rm


def test_rm_function():
    """
        Тесты команды rm
    """
    assert rm('tests/test2.zip') == 0
    assert rm(os.path.abspath('.history')) == 0
