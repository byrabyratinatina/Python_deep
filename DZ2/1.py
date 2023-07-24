"""
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""
num = int(input('Введите число в десятичной системе: '))


def self_hex(numbers: int) -> str:
    if not numbers:
        return '0x0'
    results = ''
    hex_letters = list('0123456789abcdef')
    while numbers > 0:
        results = hex_letters[numbers % 16] + results
        numbers //= 16
    return '0x' + results
    pass


self_hex(num)
print(f'Встроенная функция hex -> \t\t{hex(num)}')
print(f'Собственная функция self_hex -> {self_hex(num)}')


