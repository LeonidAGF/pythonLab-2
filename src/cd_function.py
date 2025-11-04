import os
import logging


def cd(path: str) -> int:
    """
    функция реализующая команду cd, которая меняет текущий католог на тот, который передан через path
    :return: возращает 1 если при выполнении произошла ошибка, иначе возвращет 0
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
