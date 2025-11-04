from src.cp_function import cp
from src.mv_function import mv


def test_mv_function():
    """
        Тесты команды mv
    """
    cp('requirements.txt', 'test2.zip', '')
    assert mv('test2.zip', './tests') == 0
