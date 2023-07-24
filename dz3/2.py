'''
Задача 2:
Дан список повторяющихся элементов.
Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
'''

list_1 = [9, 9, 1, 2, 9, 4, 3, 3, 1, 1, 5, 6, 6, 9, 7, 7, 3]
double = []
i = 0

while i < len(list_1):
    if list_1.count(list_1[i]) > 1:
        for _ in range(1, (list_1.count(list_1[i]))):
            double.append(list_1.pop(list_1.index(list_1[i], i + 1)))
    i += 1

print(f"Дубликаты:             {double}")
print(f"Результирующий список: {list_1}")