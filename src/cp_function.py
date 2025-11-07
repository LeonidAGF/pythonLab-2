import os.path
import shutil
import logging

from src.constants import WRITING_COMMAND_ERROR


def cp(from_path: str, to_path: str, flag: str) -> int:
    """
    функция реализующая команду cp, которая копирует файл или папку с её содержиммым или без.
    :return: возращает 1 если при выполнении произошла ошибка, иначе возвращет 0
    """
    try:

        if os.path.isdir(from_path):
            if flag == '-r':
                shutil.copytree(from_path, to_path)
            elif flag != '':
                raise Exception(WRITING_COMMAND_ERROR)
            else:
                os.mkdir(to_path)
        else:
            shutil.copy(from_path, to_path)

    except Exception as e:
        logging.error(e)
        return 1
    logging.info('cp ' + from_path + ' ' + to_path)
    return 0
