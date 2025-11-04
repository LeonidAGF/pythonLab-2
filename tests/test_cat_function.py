import os

from src.cat_function import cat


def test_cat_function():
    """
        Тесты для команды cat
    """
    assert cat('./tests/test_cat_function.py')==0
    assert cat('requirements.txt')==0
    assert cat(os.path.abspath('requirements.txt'))==0
    assert cat(os.path.abspath('./tests/test_cat_function.py'))==0
