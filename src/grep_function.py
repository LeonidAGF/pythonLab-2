import logging
import os
import re


def grep(pattern:str, path:str, flags:list()) -> int:
    """
    функция реализующая команду grep, которая исчет вхождение pattern в один из файлов котолога, находящегося по пути path.
    Если flags содержат -r, то при встрече католога функция проверит вхождение pattern в один из файлов котолога при помощи вызова себя с path встреченного каталога.
    :return: возращает 1 если при выполнении произошла ошибка, иначе возвращет 0
    """
    try:

        if path[-1]!='/' and path[-1]!='\\':
            path+='/'

        files_in_directory = os.listdir(path)
        for el in files_in_directory:
            if os.path.isfile(path+el):
                data:list()=open(path+el).readlines()
                for line_num in range(0,len(data)):
                    match: re.Match
                    if '-i' in flags:
                        match = re.search(pattern,data[line_num],re.IGNORECASE)
                    else:
                        match = re.search(pattern, data[line_num])
                    if match!=None:
                        print(path+el+' '+str(data[line_num])+' line number '+str(line_num+1))
            else:
                if '-r' in flags:
                    grep(pattern,path+el+'/',flags)
    except Exception as e:
        logging.error(e)
        return 1
    flags_string:str = ''
    for el in flags:
        flags_string+=el+' '
    logging.info('grep ' + flags_string + ' '+pattern + ' '+path)
    return 0
