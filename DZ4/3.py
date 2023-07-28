"""
Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
✔ Любое действие выводит сумму денег
"""

from datetime import date

summ = 0
count = 0


def add_bank(cash: float):
    global summ
    global count
    summ += cash
    count += 1
    if count % 3 == 0:
        summ = summ + 0.03 * summ
        print("начислены проценты в размере: ", 0.03 * summ)


def out_bank(cash: float):
    global summ
    global count
    summ -= cash
    count += 1
    comission = 0.015 * cash
    if comission < 30:
        tax = 30
    elif comission > 600:
        tax = 600
    else:
        tax = comission
    summ -= tax
    print("списаны проценты за снятие: ", tax)
    if count % 3 == 0:
        summ = summ + 0.03 * summ
        print("начислены проценты в размере: ", 0.03 * summ)


def check_bank():
    while True:
        cash = int(input("Введите сумму опреации кратно 50 : "))
        if cash % 50 == 0:
            return cash
        else:
            print("Введена некорректная сумма (некратна 50)")


log_operation = []

while True:
    action = input('о - снять деньги\na - пополнить\nh - история операций\nq - выйти\n')
    if summ > 5_000_000:
        summ = summ - 0.1 * summ  
        print(f'списан налог на богатство: {0.1 *  summ}')
        print(f'Текущий баланс = {summ}')
    if action == 'o':
        cash = check_bank()
        if cash < summ:
            out_bank(cash)
            log_operation.append([str(date.today()), -cash])
        else:
            print('недостаточно средств\n')
        print(f'Текущий баланс = {summ}')
    elif action == 'a':
        cash = check_bank()
        add_bank(cash)
        log_operation.append([str(date.today()), cash])
        print(f'Текущий баланс = {summ}')
    elif action == 'h':
        print('история операций:')
        print(log_operation)
        print(f'Текущий баланс = {summ}')
    else:
        print("Выход из банкомата")
        exit()
    
    
