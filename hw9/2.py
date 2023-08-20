from random import randint


# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами из диапазонов.
#
# декоратор должен проверять значения функции угадайка чтобы были в допустимых пределах
# то есть в декораторе будет обертка  wrapper  для любой функции (fun), которая будет передана в декоратор
# декоратор возвращает обертку wrapper
def func_enigma(func):
    def wrapper(q_num: int, attempts: int):
        q_num = q_num if 1 < q_num < 100 else randint(1, 100)
        attempts = attempts if 1 < attempts < 10 else randint(1, 10)
        # print(q_num, attempts)
        res = func(q_num, attempts)
        return res

    return wrapper


@func_enigma
def attempts_count(q_num, attempts):
    while attempts > 0:
        num = int(input(f'Я загадал число от 1 до 100. Угадай:> '))
        if num == q_num:
            return "Угадал!"
        attempts -= 1
        if num < q_num:
            print('Больше!')
        else:
            print('Меньше!')
        print(f'осталось {attempts} попыток')
    return "Не угадал."


# Функция принимает на вход три целых числа:
# нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
def func(start, stop, count):
    num = randint(start, stop)
    i = 0
    while count > i:
        u_num = int(input(f"введите число в диапазоне от {start} до {stop}:>"))
        if u_num > num:
            print('меньше!')
        elif u_num < num:
            print('больше!')
        else:
            print('Угадал!')
            return True
        i += 1
    return False


# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.
def func_1(qws, ans, count):
    print(f"загадка: {qws}")
    print(f"варианты ответов: {ans}")
    i = 0
    while count >= i:
        u_ans = input(f"введите ваш ответ:>")
        if u_ans == ans[0]:
            print(f'Правильно! Угадал за {i + 1} попытку')
            return i + 1
        else:
            print('Не угадал!')
            i += 1
        if i == count:
            return 0


# Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.
def func_2(dct):
    for k, v in dct.items():
        print(func_1(k, v, 3))


if __name__ == '__main__':
    # 1)
    print(attempts_count(105, 25))
    # 2)
    # print(func(1, 3, 3))
    # 3)
    # print(func_1("Не лает, не кусает, в дом не пускает",
    #              ['замок', 'охранник', 'собака'], 3))
    # # 4)
    # dct = {"В чем сила: ": ['в правде', 'в деньгах', 'в силе'],
    #        "Не лает, не кусает, в дом не пускает": ['замок', 'охранник', 'собака']}
    # func_2(dct)