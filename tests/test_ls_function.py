import os

from src.ls_function import ls


def test_ls_function():
    """
        Тесты с неправильными командами
    """
    assert ls('', '') == 0
    assert ls('', '-l') == 0
    assert ls(os.path.abspath('tests'), '') == 0
    assert ls('tests', '-l') == 0
    assert ls('tests', '') == 0
