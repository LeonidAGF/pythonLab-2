import os
import logging
import shutil

from src.constants import TRASH_FILE_PATH
from src.mv_function import mv


def rm(path: str, flag: str) -> int:
    """
    функция реализующая команду rm, перемещает файл или католог в католог .trash
    :return: возращает 1 если при выполнении произошла ошибка, иначе возвращет 0
    """
    try:
        if os.path.isdir(TRASH_FILE_PATH)==0:
            os.mkdir(TRASH_FILE_PATH)

        if path == '/' or path == '..' or path=='.' or path=='':
            raise Exception

        #elif os.path.isdir(path):
        #    if flag == '-r':
        #        shutil.rmtree(path)
        #    elif flag != '':
        #        raise Exception('Error in writing the command')
        #    else:
        #        os.rmdir(path)
        #else:
        #    os.remove(path)

        mv(path,TRASH_FILE_PATH)

    except Exception as e:
        logging.error(e)
        return 1
    logging.info('rm ' + path)
    return 0

def rm_with_permission(path: str, flag: str) -> int:
    """
    функция реализующая команду rm, перемещает файл или католог в католог .trash, получив согласие пользователя
    :return: возращает 1 если при выполнении произошла ошибка, иначе возвращет 0
    """
    try:
        answer:str = str(input('Удалить '+path+'? (y/n)'))
        if 'y'==answer:
            if os.path.isdir(TRASH_FILE_PATH)==0:
                os.mkdir(TRASH_FILE_PATH)

            if path == '/' or path == '..' or path=='.' or path=='':
                raise Exception

            mv(path,TRASH_FILE_PATH)

    except Exception as e:
        logging.error(e)
        return 1
    logging.info('rm ' + path)
    return 0
