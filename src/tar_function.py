import tarfile
import logging
import os


def un_tar_file(path: str, path_to: str) -> int:
    """
    Точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """
    try:
        t = tarfile.open(path, 'r:gz')
        t.extractall(path_to)
        t.close()
    except Exception as e:
        logging.error(e)
        return 1
    logging.info('untar ' + path + ' ' + path_to)
    return 0


def tar_file(path: str,name:str) -> int:
    """
    Точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """
    try:
        t = tarfile.open(path+'/'+name, 'w:gz')
        files_in_directory = os.listdir(path)
        for name_of_file in files_in_directory:
            t.add(name_of_file)
        t.close()
    except Exception as e:
        logging.error(e)
        return 1
    logging.info('tar ' + path)
    return 0
