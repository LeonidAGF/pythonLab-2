import os
import logging
from src.cat_function import cat
from src.cd_function import cd
from src.cp_function import cp
from src.ls_function import ls
from src.mv_function import mv
from src.parse_command import parse_command
from src.rm_function import rm
from src.tar_function import tar_file, un_tar_file
from src.zip_function import zip_file, un_zip_file

def main() -> None:
    """
    Точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """

    logging.basicConfig(level=logging.DEBUG, filename="shell.log", filemode="a", datefmt='%Y-%m-%d %H:%M:%S',
                        format="[%(asctime)s] %(levelname)s %(message)s")

    print('Здравствуйте '+os.getlogin())
    print('Текущая директория: '+os.getcwd())

    while (1):

        command:str = input('')
        parsed_cmd:list() = parse_command(command)

        try:
            if len(parsed_cmd)==0:
                raise Exception
            match parsed_cmd[0]:
                case 'cat':
                    cat(parsed_cmd[1])
                case 'cd':
                    cd(parsed_cmd[1])
                case 'cp':
                    if len(parsed_cmd) < 4:
                        cp(parsed_cmd[3],parsed_cmd[2],'')
                    else:
                        cp(parsed_cmd[2],parsed_cmd[3],parsed_cmd[1])
                case 'ls':
                    if len(parsed_cmd)==1:
                        ls('','')
                    elif len(parsed_cmd)==2:
                        ls('', parsed_cmd[1])
                    else:
                        ls(parsed_cmd[2],parsed_cmd[1])
                case 'mv':
                    mv(parsed_cmd[1],parsed_cmd[2])
                case 'rm':
                    if len(parsed_cmd)<3:
                        rm(parsed_cmd[1],'')
                    else:
                        rm(parsed_cmd[2],parsed_cmd[1])
                case 'tar':
                    tar_file(parsed_cmd[1],parsed_cmd[2])
                case 'untar':
                    un_tar_file(parsed_cmd[1],parsed_cmd[2])
                case 'zip':
                    zip_file(parsed_cmd[1],parsed_cmd[2])
                case 'unzip':
                    un_zip_file(parsed_cmd[1],parsed_cmd[2])
        except Exception:
            logging.error("Error in writing the command")


if __name__ == "__main__":
    main()
