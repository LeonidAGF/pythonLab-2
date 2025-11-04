import logging

from src.constants import HISTORY_FILE_PATH


def history(n: int) -> int:
    """
    функция реализующая команду history, выводит в консоль n последних команд
    :return: возращает 1 если при выполнении произошла ошибка, иначе возвращет 0
    """
    try:

        data: list[str] = [str(el) for el in open(HISTORY_FILE_PATH, 'r')]
        for command in data[-n:len(data)]:
            print(command.replace('\n', ''))

    except Exception as e:
        logging.error(e)
        return 1
    logging.info('history ' + str(n))
    return 0


def history_write(command: str) -> int:
    """
    функция реализующая команду history, записывает выполненную команду в файл .history
    :return: возращает 1 если при выполнении произошла ошибка, иначе возвращет 0
    """
    try:
        open(HISTORY_FILE_PATH, 'a').close()
        data: list[str] = [str(el) for el in open(HISTORY_FILE_PATH, 'r')]
        last_num: int = 1
        if len(data) > 0:
            last_num = int(data[-1].split()[0]) + 1
        file = open(HISTORY_FILE_PATH, 'a')
        file.write(str(last_num) + ' ' + command + '\n')
        file.close()

    except Exception as e:
        logging.error(e)
        return 1
    return 0
