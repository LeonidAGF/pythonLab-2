import os

from src.rm_function import rm
from src.tar_function import tar_file, un_tar_file


def test_tar_function():
    """
        Тесты команд tar и untar
    """
    assert tar_file('./', 'test3.gz') == 0
    assert un_tar_file('test3.gz', os.path.abspath('testdir/')) == 0
    rm('test3.gz', '-r')
