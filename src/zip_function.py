import os
from zipfile import ZipFile
import logging


def zip_file(from_path: str, to_path: str) -> int:
    """
    функция реализующая команду zip, создаёт zip архив
    :return: возращает 1 если при выполнении произошла ошибка, иначе возвращет 0
    """
    try:
        files_in_directory = os.listdir(from_path)
        z = ZipFile(to_path, 'w')
        origin_path:str = os.path.abspath('')
        os.chdir(from_path)
        for name_of_file in files_in_directory:
            z.write(name_of_file)
        os.chdir(origin_path)
        z.close()
    except Exception as e:
        logging.error(e)
        return 1
    logging.info('zip ' + from_path + ' ' + to_path)
    return 0


def un_zip_file(from_path: str, to_path: str) -> int:
    """
    функция реализующая команду zip, разархивирует zip архив
    :return: возращает 1 если при выполнении произошла ошибка, иначе возвращет 0
    """
    try:
        z = ZipFile(from_path, 'r')
        z.extractall(to_path)
        z.close()
    except Exception as e:
        logging.error(e)
        return 1
    logging.info('unzip ' + from_path + ' ' + to_path)
    return 0
