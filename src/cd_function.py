import os
import logging


def cd(path: str) -> int:
    """
    Точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """
    try:
        if path == '~':
            os.chdir(os.path.expanduser("~"))
        else:
            os.chdir(path)
        print("Каталог изменен на: " + os.getcwd())
    except Exception as e:
        logging.error(e)
        return 1
    logging.info('cd ' + path)
    return 0
