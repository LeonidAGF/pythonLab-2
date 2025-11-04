import logging


def cat(path: str) -> int:
    """
    функция реализующая команду cat, которая выводит в консоль текст файла
    :return: возращает 1 если при выполнении произошла ошибка, иначе возвращет 0
    """
    try:
        print(str(open(path).read()))
    except Exception as e:
        logging.error(e)
        return 1
    logging.info('cat ' + path)
    return 0
