from src.cd_function import cd
from src.cp_function import cp
from src.history_function import history
from src.input_function import input_function
from src.ls_function import ls
from src.mv_function import mv
from src.rm_function import rm
from src.tar_function import un_tar_file
from src.zip_function import un_zip_file


def test_incorrect_tests():
    """
        Тесты с неправильными командами
    """
    assert ls('', '-r') == 1
    assert rm('', '-l') == 1
    assert rm('.', '') == 1
    assert rm('..', '') == 1
    assert cp('', '', '-l') == 1
    assert cp('test_cat_function.py', './test1', '') == 1
    assert cp('./test', 'test1', '-r') == 1
    assert cd('./test') == 1
    assert history('') == 1
    assert input_function('ne_comanda') == 1
    assert input_function('') == 1
    assert input_function('') == 1
    assert mv('tests1', 'test1') == 1
    assert un_tar_file('tests1', 'test1') == 1
    assert un_zip_file('tests1', 'test1') == 1
