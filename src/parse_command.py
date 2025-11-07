import re


def parse_command(command: str) -> list[str]:
    """
    функция parse_command, превращает команду, введённую пользователем, в массив токенов.
    :return: возращает 1 если при выполнении произошла ошибка, иначе возвращет 0
    """
    tokens = re.findall(
        r"cat|cd|cp|ls|mv|rm|tar|untar|zip|unzip|history|undo|grep|[1-9]{1,}|-l|-r|-i|\.\.|(?:[a-zA-Z.0-9\-_*?<>()|{}+!@#$%^&а-яА-Я]{0,}[~/\\:]{0,1}){1,}",
        command)
    while '' in tokens:
        tokens.remove('')
    return tokens
