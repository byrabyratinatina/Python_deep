"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
"""
from fractions import Fraction

first_fact = input('Введите первую дробь формата "a/b": ').split('/')
second_fact = input('Введите вторую дробь формата "a/b": ').split('/')


class SelfFraction:
    def __init__(self, numerator: int, denominator: int):
        if not isinstance(numerator, int) and not isinstance(denominator, int):
            raise ValueError
        elif denominator == 0:
            raise ZeroDivisionError
        else:
            nod = SelfFraction.check_nod(numerator, denominator)
            self.num = numerator // nod
            self.den = denominator // nod

    def __add__(self, other):
        main_den = self.den * other.den
        main_num = self.num * other.den + other.num * self.den
        return SelfFraction(main_num, main_den)

    def __mul__(self, other):
        main_num = self.num * other.num
        main_den = self.den * other.den
        return SelfFraction(main_num, main_den)

    @staticmethod
    def check_nod(numbers: int, den: int) -> int:
        nod = 1
        for i in range(1, max(numbers, den) // 2 + 1):
            if numbers % i == 0 and den % i == 0:
                nod = i
        return nod

    def __str__(self):
        return f'{self.num}/{self.den}'


self_fact_1 = SelfFraction(int(first_fact[0]), int(first_fact[1]))
self_fact_2 = SelfFraction(int(second_fact[0]), int(second_fact[1]))

original_fact_1 = Fraction(int(first_fact[0]), int(first_fact[1]))
original_fact_2 = Fraction(int(second_fact[0]), int(second_fact[1]))

print(f'Свой класс {self_fact_1 + self_fact_2}')
print(f'Проверка {original_fact_1 + original_fact_2}')

print(f'Свой класс {self_fact_1 * self_fact_2}')
print(f'Проверка {original_fact_1 * original_fact_2}')
