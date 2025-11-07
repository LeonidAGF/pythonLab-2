import logging
from src.cat_function import cat
from src.cd_function import cd
from src.constants import WRITING_COMMAND_ERROR
from src.cp_function import cp
from src.grep_function import grep
from src.history_function import history, history_write
from src.ls_function import ls
from src.mv_function import mv
from src.parse_command import parse_command
from src.rm_function import rm_with_permission
from src.tar_function import tar_file, un_tar_file
from src.undo_function import undo
from src.zip_function import zip_file, un_zip_file


def input_function(command: str) -> int:
    """
    функция  input_function, получает на вход команду введённую пользователем, преобразует её в массив токенов и выполняет консольную команду соответствующую введённым данным.
    :return: возращает 1 если при выполнении произошла ошибка, иначе возвращет 0
    """
    parsed_cmd: list[str] = parse_command(command)

    try:
        if len(parsed_cmd) == 0:
            raise Exception
        match parsed_cmd[0]:
            case 'cat':

                if len(parsed_cmd)>2:
                    raise Exception
                cat(parsed_cmd[1])

            case 'cd':

                if len(parsed_cmd) > 2:
                    raise Exception
                cd(parsed_cmd[1])

            case 'cp':
                if len(parsed_cmd) > 4:
                    raise Exception
                elif len(parsed_cmd) < 4:
                    cp(parsed_cmd[1], parsed_cmd[2], '')
                else:
                    cp(parsed_cmd[2], parsed_cmd[3], parsed_cmd[1])
            case 'ls':

                if len(parsed_cmd) > 3:
                    raise Exception
                elif len(parsed_cmd) == 1:
                    ls('', '')
                elif len(parsed_cmd) == 2:
                    ls(parsed_cmd[1], '')
                else:
                    ls(parsed_cmd[2], parsed_cmd[1])

            case 'mv':

                if len(parsed_cmd) > 3:
                    raise Exception
                mv(parsed_cmd[1], parsed_cmd[2])

            case 'rm':

                if len(parsed_cmd) > 3:
                    raise Exception
                elif len(parsed_cmd) < 3:
                    rm_with_permission(parsed_cmd[1])
                else:
                    rm_with_permission(parsed_cmd[2])

            case 'tar':

                if len(parsed_cmd) > 3:
                    raise Exception
                tar_file(parsed_cmd[1],parsed_cmd[2])

            case 'untar':

                if len(parsed_cmd) > 3:
                    raise Exception
                un_tar_file(parsed_cmd[1], parsed_cmd[2])

            case 'zip':

                if len(parsed_cmd) > 3:
                    raise Exception
                zip_file(parsed_cmd[1], parsed_cmd[2])

            case 'unzip':

                if len(parsed_cmd) > 3:
                    raise Exception
                un_zip_file(parsed_cmd[1], parsed_cmd[2])

            case 'history':

                if len(parsed_cmd) > 2:
                    raise Exception
                history(int(parsed_cmd[1]))

            case 'undo':

                if len(parsed_cmd) > 1:
                    raise Exception
                undo()

            case 'grep':

                if len(parsed_cmd) > 5:
                    raise Exception
                elif len(parsed_cmd)==3:
                    grep(parsed_cmd[2],parsed_cmd[1],[])
                elif len(parsed_cmd)==4:
                    grep(parsed_cmd[3],parsed_cmd[2],[parsed_cmd[1]])
                else:
                    grep(parsed_cmd[4],parsed_cmd[3],[parsed_cmd[2],parsed_cmd[1]])
            case _:
                raise Exception

        history_write(command)

    except Exception:
        logging.error(WRITING_COMMAND_ERROR)
        return 1
    return 0
