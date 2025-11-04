import os
from zipfile import ZipFile
import logging


def zip_file(from_path: str, to_path: str) -> int:
    """
    Точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """
    try:
        z = ZipFile(to_path, 'w')
        files_in_directory = os.listdir(from_path)
        for name_of_file in files_in_directory:
            z.write(name_of_file)
        z.close()
    except Exception as e:
        logging.error(e)
        return 1
    logging.info('zip ' + from_path + ' ' + to_path)
    return 0


def un_zip_file(from_path: str, to_path: str) -> int:
    """
    Точкой входа в приложение
    :return: Данная функция ничего не возвращает
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
