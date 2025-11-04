import logging

from src.constants import HISTORY_FILE_PATH, TRASH_FILE_PATH
from src.mv_function import mv
from src.parse_command import parse_command
from src.rm_function import rm


def undo() -> int:
    """
    функция реализующая команду undo, отменяет действие команд: rm, cp, mv. Работает при условии ввода сразу после исполнения команды, которую хочется отменить.
    :return: возращает 1 если при выполнении произошла ошибка, иначе возвращет 0
    """
    try:
        command_list_from_file: list[str] = open(HISTORY_FILE_PATH, 'r').readlines()
        if len(command_list_from_file) - 1 > -1:
            command_without_index = 0
            while command_list_from_file[-1][command_without_index] in '0123456789':
                command_without_index += 1
            command: str = command_list_from_file[-1][command_without_index:len(command_list_from_file[-1])]
            command_list: list[str] = parse_command(command)
            if command_list[0] in 'cp mv rm':
                match command_list[0]:
                    case 'cp':
                        rm(command_list[2], '-r')
                    case 'mv':
                        from_path: str = command_list[1]
                        mv_name: str = ''
                        if len(from_path) > 0:
                            while len(from_path) > 0 and from_path[-1] != '/' and from_path[-1] != '\\':
                                mv_name = from_path[-1] + mv_name
                                from_path = from_path[0:len(from_path) - 1]
                        if from_path == '':
                            from_path = './'
                        if command_list[2][-1] != '\\' or command_list[2][-1] != '/':
                            command_list[2] += '/'
                        mv(command_list[2] + mv_name, from_path)
                    case 'rm':
                        rm_from_path: str = command_list[1]
                        rm_name: str = ''
                        while len(rm_from_path) > 0 and rm_from_path[-1] != '/' and rm_from_path[-1] != '\\':
                            rm_name = rm_from_path[-1] + rm_name
                            rm_from_path = rm_from_path[0:len(rm_from_path) - 1]
                        if rm_from_path == '':
                            rm_from_path = './'
                        mv(TRASH_FILE_PATH + '/' + rm_name, rm_from_path + rm_name)
    except Exception as e:
        logging.error(e)
        return 1
    logging.info('undo')
    return 0
