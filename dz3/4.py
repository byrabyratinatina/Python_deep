'''
Задача 4:
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.
'''

camping_kit = {"Спички": 1, "Туалетная бумага": 1, "Вода": 1, "Еда": 2, "Фонарик": 1, "Нож": 1\
               "Куртка": 5, "Ложка": 1, "Чайник": 4, "Палатка": 12}
list_inventory = []
size = int(input("Введите размер рюкзака в кг.: "))
remained = []

for key, value in camping_kit.items():
    if value <= size:
        size -= value
        list_inventory.append(key)

if len(camping_kit) > len(list_inventory):
    for invent in camping_kit:
        if invent not in list_inventory:
            remained.append(invent)
    print(f"Поместилось {list_inventory}, не поместилось {remained}")
else:
    print(f"Постилось {list_inventory}, ничего не осталось")