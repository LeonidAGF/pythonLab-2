import os.path
import shutil
import logging

from src.constants import HISTORY_FILE_PATH


def history(n: int) -> int:
    """
    Точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """
    try:

        data: list() = [str(el) for el in open(HISTORY_FILE_PATH, 'r')]
        for command in data[-n:len(data)]:
            print(command.replace('\n', ''))

    except Exception as e:
        logging.error(e)
        return 1
    logging.info('history ' + str(n))
    return 0


def history_write(command: str) -> int:
    """
    Точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """
    try:
        open(HISTORY_FILE_PATH, 'w').close()
        data: list() = [str(el) for el in open(HISTORY_FILE_PATH, 'r')]
        last_num: int = 1
        if len(data) > 0:
            last_num = int(data[-1].split()[0]) + 1
        file = open(HISTORY_FILE_PATH, 'a')
        file.write(str(last_num) + ' ' + command + '\n')
        file.close()

    except Exception as e:
        logging.error(e)
        return 1
    return 0
