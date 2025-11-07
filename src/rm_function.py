import os
import logging
import re

from src.constants import TRASH_FILE_PATH, WRITING_COMMAND_ERROR
from src.mv_function import mv


def rm(path: str) -> int:
    """
    функция реализующая команду rm, перемещает файл или католог в католог .trash
    :return: возращает 1 если при выполнении произошла ошибка, иначе возвращет 0
    """
    try:
        if os.path.isdir(TRASH_FILE_PATH)==0:
            os.mkdir(TRASH_FILE_PATH)

        if len(path)==0 or path == '/' or path== '\\' or path == '..' or path == '.' or path == '' or (re.search(r'[A-Z]:(?:\\|/)', path) and len(path) == 3):
            raise Exception(WRITING_COMMAND_ERROR)

        mv(path,TRASH_FILE_PATH)

    except Exception as e:
        logging.error(e)
        return 1
    logging.info('rm ' + path)
    return 0

def rm_with_permission(path: str) -> int:
    """
    функция реализующая команду rm, перемещает файл или католог в католог .trash, получив согласие пользователя
    :return: возращает 1 если при выполнении произошла ошибка, иначе возвращет 0
    """
    try:
        answer:str = str(input('Удалить '+path+'? (y/n)'))
        if answer=='y':
            rm(path)

    except Exception as e:
        logging.error(e)
        return 1
    return 0
