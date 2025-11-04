import tarfile
import logging
import os


def un_tar_file(path: str, path_to: str) -> int:
    """
    функция реализующая команду untar, разархивирует tar архив
    :return: возращает 1 если при выполнении произошла ошибка, иначе возвращет 0
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
    функция реализующая команду tar, создаёт tar архив
    :return: возращает 1 если при выполнении произошла ошибка, иначе возвращет 0
    """
    try:
        files_in_directory = os.listdir(path)
        t = tarfile.open(path+'/'+name, 'w:gz')
        origin_path: str = os.path.abspath('')
        os.chdir(path)
        for name_of_file in files_in_directory:
            t.add(name_of_file)
        os.chdir(origin_path)
        t.close()
    except Exception as e:
        logging.error(e)
        return 1
    logging.info('tar ' + path)
    return 0
