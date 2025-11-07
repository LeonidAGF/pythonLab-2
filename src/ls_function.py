import logging
import os
import datetime

from src.constants import WRITING_COMMAND_ERROR


def ls(path: str, flag: str) -> int:
    """
    функция реализующая команду ls, выводит в консоль имена файлов и катологов, расположенных по путю path.
    :return: возращает 1 если при выполнении произошла ошибка, иначе возвращет 0
    """
    try:
        if path == '':
            path = os.getcwd()
        files_in_directory = os.listdir(path)
        for el in files_in_directory:
            res: str = el
            if flag == '-l':
                file_path: str = path + '/' + el

                read_writeexecute_permissions: str = ''

                if os.access(file_path, os.R_OK):
                    read_writeexecute_permissions += 'r'
                if os.access(file_path, os.W_OK):
                    read_writeexecute_permissions += 'w'
                if os.access(file_path, os.X_OK):
                    read_writeexecute_permissions += 'x'

                res = read_writeexecute_permissions + ' ' + ' ' + datetime.datetime.fromtimestamp(
                    os.path.getmtime(file_path)).strftime('%d.%m.%Y %H:%M:%S') + ' ' + str(
                    os.path.getsize(file_path)) + ' byte ' + res
            elif flag != '':
                raise Exception(WRITING_COMMAND_ERROR)
            print(res)
    except Exception as e:
        logging.error(e)
        return 1
    logging.info('ls ' + path)
    return 0
