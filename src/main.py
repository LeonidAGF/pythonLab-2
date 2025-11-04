from src.input_function import input_function
import os
import logging


def main() -> None:
    """
    Точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """

    logging.basicConfig(level=logging.DEBUG, filename="shell.log", filemode="a", datefmt='%Y-%m-%d %H:%M:%S',
                        format="[%(asctime)s] %(levelname)s %(message)s")

    print('Здравствуйте ' + os.getlogin())
    print('Текущая директория: ' + os.getcwd())

    while (1):
        command: str = input('')
        input_function(command)


if __name__ == "__main__":
    main()
