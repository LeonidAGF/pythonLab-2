from src.cp_function import cp
from src.history_function import history_write
from src.mv_function import mv
from src.rm_function import rm
from src.undo_function import undo


def test_undo_function():
    """
        Тесты команды undo
    """
    cp('pyproject.toml','t1','')
    history_write('cp pyproject.toml t1')
    assert undo() == 0
    cp('pyproject.toml', 't2','')
    rm('t2')
    history_write('rm t2')
    assert undo() == 0
    mv('t2','.trash')
    history_write('mv t2 .trash')
    assert undo() == 0
    rm('t2')
