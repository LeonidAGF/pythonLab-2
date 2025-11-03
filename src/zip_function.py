from zipfile import ZipFile
import logging

def zip_file(from_path:str, to_path:str) -> int:
    try:
        z = ZipFile(to_path, 'w')
        z.write(from_path)
        z.close()
    except Exception as e:
        logging.error(e)
        return 1
    logging.info('zip ' + from_path + ' ' + to_path)
    return 0

def un_zip_file(from_path:str, to_path:str) -> int:
    try:
        z = ZipFile(from_path, 'r')
        z.extractall(to_path)
        z.close()
    except Exception as e:
        logging.error(e)
        return 1
    logging.info('unzip ' + from_path + ' ' + to_path)
    return 0