'''
Задача 3:
Создайте функцию генератор чисел Фибоначчи (см. Википедию).
'''

#Функция вычисления числа Фибоначчи
def fib(n):
    if n in (1, 2):
        return 1
    return fib(n - 1) + fib(n - 2)

#Функция генератор чисел Фибоначчи
def fib_generator(n):
    for i in range(1, n + 1):
        yield f"{i} число фибоначчи = {fib(i)}"


num = 10
iter_fib_generator = iter(fib_generator(num))
print(next(iter_fib_generator))
print(next(iter_fib_generator))
print(next(iter_fib_generator))
print(next(iter_fib_generator))
print(next(iter_fib_generator))

# Второй вариант с циклом
def fib_for(arg):
    fib1 = 1
    fib2 = 1
    for i in range(arg):
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        yield fib_sum

num = 10
print("\nВариант с циклом ->")
iter_fib_for = iter(fib_for(num))
print(next(iter_fib_for),
      next(iter_fib_for),
      next(iter_fib_for),
      next(iter_fib_for),
      next(iter_fib_for))

print("\n\nРабота рекурсии \n")

def recursive(value):
    print(value)
    if value < 3:
        recursive(value + 1)
    print(value)

recursive(1)
