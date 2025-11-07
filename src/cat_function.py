import logging


def cat(path: str) -> int:
    """
    функция реализующая команду cat, которая выводит в консоль текст файла
    :return: возращает 1 если при выполнении произошла ошибка, иначе возвращет 0
    """
    try:

        file = open(path, 'r')
        file_text: str = file.read()
        file.close()

        print(file_text)
    except Exception as e:
        logging.error(e)
        return 1
    logging.info('cat ' + path)
    return 0
