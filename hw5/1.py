'''
Задача 1:
Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла.
'''


def file_path(data):
    data = data.replace(".", " ").replace("\\", " ")
    *way, name, extension = data.split()
    res = "\\".join(way), name, extension
    return res

path = "C:\Program Files\Windows Security\BrowserCore\manifest.json"
print(file_path(path))