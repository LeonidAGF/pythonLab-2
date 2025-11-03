import shutil
import logging

def mv(from_path:str,to_path:str) -> int:
    try:
        shutil.move(from_path,to_path)
    except Exception as e:
        logging.error(e)
        return 1
    logging.info('mv ' + from_path + ' ' + to_path)
    return 0