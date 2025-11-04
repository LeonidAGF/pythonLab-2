import re


def parse_command(command: str) -> list():
    """
    Точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """
    tokens = re.findall(
        r"cat|cd|cp|ls|mv|rm|tar|untar|zip|unzip|history|[1-9]{1,}|-l|-r|\.\.|(?:[a-zA-Z.0-9\-]{0,}[~/\\:]{0,1}){1,}",
        command)
    while '' in tokens:
        tokens.remove('')
    return tokens
