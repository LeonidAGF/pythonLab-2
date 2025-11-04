import os

from src.cd_function import cd


def test_cd_function():
        """
            Тесты для команды
        """
        path:str = os.path.abspath('')
        assert cd('./tests') == 0
        assert cd('..') == 0
        assert cd(os.path.abspath('./tests')) == 0
        assert cd('~') == 0
        assert cd(path) == 0
