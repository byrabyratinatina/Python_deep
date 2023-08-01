from datetime import datetime

__all__ = ['check_year', 'date_validator']


"""
Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999]. 
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь. 
Проверку года на високосность вынести в отдельную защищённую функцию.
"""


def _check_leap_year(date: str) -> bool:
    check_normal_1 = 4
    check_normal_2 = 100
    check_normal_3 = 400
    years = range(1, 10000)
    year = int(date.split(".")[-1])
    if year in years and year % check_normal_1 == 0 and year % check_normal_2 != 0 or year % check_normal_3 == 0:
        return True
    return False


def check_year(year: str) -> bool:
    try:
        _ = datetime.strptime(year, "%d.%m.%Y").date()
        return True
    except ValueError:
        return False


def date_validator(date: str) -> str:
    if check_year(date):
        return 'Високосный' if _check_leap_year(date) else 'Не является высокосным'
    else:
        return f'Дата заполнена некорректно'