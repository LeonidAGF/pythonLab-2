import logging
import os
import datetime


def ls(path:str,flag:str) -> int:
    try:
        if path=='':
            path=os.getcwd()
        files_in_directory = os.listdir(path)
        for el in files_in_directory:
            res:str = el
            if flag == '-l':
                file_path:str = path + '/' + el

                read_writeexecute_permissions:str = ''

                if os.access(file_path,os.R_OK):
                    read_writeexecute_permissions += 'r'
                if os.access(file_path,os.W_OK):
                    read_writeexecute_permissions += 'w'
                if os.access(file_path,os.X_OK):
                    read_writeexecute_permissions += 'x'

                res = read_writeexecute_permissions + ' ' + ' ' + datetime.datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%d.%m.%Y %H:%M:%S')+' '+str(os.path.getsize(file_path))+' byte '+res
            elif flag != '':
                raise Exception('Error in writing the command')
            print(res)
    except Exception as e:
        logging.error(e)
        return 1
    logging.info('ls ' + path)
    return 0
