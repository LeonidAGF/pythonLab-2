from src.grep_function import grep


def test_grep_function():
    """
        Тесты для команды grep
    """
    assert grep('try','./tests/',[]) == 0
    assert grep('try','./tests/',['-r','-i']) == 0