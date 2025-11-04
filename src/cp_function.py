import os.path
import shutil
import logging


def cp(from_path: str, to_path: str, flag: str) -> int:
    """
    Точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """
    try:

        if os.path.isdir(from_path):
            if flag == '-r':
                shutil.copytree(from_path, to_path)
            elif flag != '':
                raise Exception('Error in writing the command')
            else:
                os.mkdir(to_path)
        else:
            shutil.copy(from_path, to_path)

    except Exception as e:
        logging.error(e)
        return 1
    logging.info('cp ' + from_path + ' ' + to_path)
    return 0
