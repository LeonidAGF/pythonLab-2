import os

from src.rm_function import rm
from src.zip_function import zip_file, un_zip_file


def test_zip_function():
    """
        Тесты команд zip и unzip
    """
    assert zip_file('testdir', 'test4.zip') == 0
    assert un_zip_file(os.path.abspath('test4.zip'), 'testdir/zpdir/') == 0
    rm('test4.zip', '-r')
