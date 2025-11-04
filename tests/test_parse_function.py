import os.path

from src.parse_command import parse_command


def test_parse_function():
    """
        Тесты функции parse_command
    """
    assert parse_command('ls -l') == ['ls', '-l']
    assert parse_command('ls -l ./') == ['ls', '-l', './']
    assert parse_command('ls -l ' + os.path.abspath('README.md')) == ['ls', '-l', os.path.abspath('README.md')]
    assert parse_command('cat ' + os.path.abspath('README.md')) == ['cat', os.path.abspath('README.md')]
    assert parse_command('ls -l                    ./') == ['ls', '-l', './']
