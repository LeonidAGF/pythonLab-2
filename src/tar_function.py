import tarfile
import logging
import os

def un_tar_file(path:str, path_to:str) -> int:
    try:
        t = tarfile.open(path, 'r:gz')
        t.extractall(path_to)
        t.close()
    except Exception as e:
        logging.error(e)
        return 1
    logging.info('untar ' + path + ' ' + path_to)
    return 0

def tar_file(path_from:str, path_to:str) -> int:
    try:
        t = tarfile.open(path_from, 'w:gz')
        files_in_directory = os.listdir(os.getcwd())
        for name_of_file in files_in_directory:
            print(name_of_file)
            t.add(name_of_file)
        t.close()
    except Exception as e:
        logging.error(e)
        return 1
    logging.info('tar ' + path_from + ' ' + path_to)
    return 0