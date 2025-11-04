import logging


def cat(path: str) -> int:
    """
    Точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """
    try:
        print(str(open(path).read()))
    except Exception as e:
        logging.error(e)
        return 1
    logging.info('cat ' + path)
    return 0
