import tarfile
import logging
import os


def un_tar_file(path: str, path_to: str) -> int:
    """
    функция реализующая команду untar, разархивирует tar архив
    :return: возращает 1 если при выполнении произошла ошибка, иначе возвращет 0
    """
    try:
        tar: tarfile.TarFile = tarfile.open(path, 'r:gz')
        tar.extractall(path_to)
        tar.close()
    except Exception as e:
        logging.error(e)
        return 1
    logging.info('untar ' + path + ' ' + path_to)
    return 0


def tar_file(path: str, name: str) -> int:
    """
    функция реализующая команду tar, создаёт tar архив
    :return: возращает 1 если при выполнении произошла ошибка, иначе возвращет 0
    """
    try:
        files_in_directory: list[str] = os.listdir(path)
        fille_path = path

        if len(fille_path) == 0 or (fille_path[-1:] != '/' and fille_path[-1:] != '\\'):
            fille_path += '/'

        tar: tarfile.TarFile = tarfile.open(path + name, 'w:gz')
        origin_path: str = os.path.abspath('')
        os.chdir(path)
        for name_of_file in files_in_directory:
            tar.add(name_of_file)
        os.chdir(origin_path)
        tar.close()

    except Exception as e:
        logging.error(e)
        return 1
    logging.info('tar ' + path)
    return 0
