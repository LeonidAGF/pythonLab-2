import shutil
import logging


def mv(from_path: str, to_path: str) -> int:
    """
    функция реализующая команду mv, перемещает файл или католог
    :return: возращает 1 если при выполнении произошла ошибка, иначе возвращет 0
    """
    try:
        shutil.move(from_path, to_path)
    except Exception as e:
        logging.error(e)
        return 1
    logging.info('mv ' + from_path + ' ' + to_path)
    return 0
