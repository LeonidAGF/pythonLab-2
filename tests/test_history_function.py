from src.history_function import history_write, history


def test_history_function():
    """
        Тесты для команды history
    """
    assert history_write('ls -l') == 0
    assert history(1) == 0
