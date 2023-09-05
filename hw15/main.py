# Возьмите любые 1-3 задачи из прошлых домашних заданий:
# - Добавьте к ним логирование ошибок и полезной информации
# - Также реализуйте возможность запуска из командной строки с передачей параметров
from sys import argv
from triangle import triangle
import argparse


triangle(6, 4, 4)
triangle(4, 3, 5)
triangle(3.5, 6, 4)

if __name__ == "__main__":
    """
    два способа вызова функции через терминал 
    с возможностью задать параметры
    """
    triangle(int(argv[1]), int(argv[2]), int(argv[3]))

    parser = argparse.ArgumentParser(description='Solving triangle')
    parser.add_argument('param', metavar='a b c', type=int, nargs=3)
    args = parser.parse_args()
    triangle(*args.param)
    