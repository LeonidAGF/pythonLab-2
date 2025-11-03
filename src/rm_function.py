import os
import logging
import shutil

def rm(path:str,flag:str) -> int:
    try:
        if os.path.isdir(path):
            if flag == '-r':
                shutil.rmtree(path)
            elif flag != '':
                raise Exception('Error in writing the command')
            else:
                os.rmdir(path)
        else:
            os.remove(path)
    except Exception as e:
        logging.error(e)
        return 1
    logging.info('rm ' + path)
    return 0