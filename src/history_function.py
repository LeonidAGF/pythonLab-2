import os.path
import shutil
import logging


def history(n: int,history_file_path:str) -> int:
    try:

        data:list() = [str(el) for el in open(history_file_path,'r')]
        for command in data[-n:len(data)]:
            print(command.replace('\n',''))

    except Exception as e:
        logging.error(e)
        return 1
    logging.info('history ' + n)
    return 0

def history_write(command:str,history_file_path:str) -> int:
    try:

        data:list() = [str(el) for el in open(history_file_path,'r')]
        last_num: int = 1
        if len(data)>0:
            last_num = int(data[-1].split()[0])+1
        file = open(history_file_path, 'a')
        file.write(str(last_num)+' '+command+'\n')
        file.close()

    except Exception as e:
        logging.error(e)
        return 1
    return 0
