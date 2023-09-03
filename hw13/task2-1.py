"""Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях. Напишите к ним классы исключения с выводом подробной информации. 
Поднимайте исключения внутри основного кода. Например нельзя создавать прямоугольник со сторонами отрицательной длины."""

class RectangleAdd(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class RectangleSub(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

class Rectangle:
    """
    Класс "Прямоугольник" для выполнения действий с прямоугольниками,
    позволяет сравнивать прямоугольники по площади,
    получить площадь и периметр прямоугольников
    складывать и вычитать прямоугольники
    """

    def __init__(self, side_a, side_b=0):
        self._width = side_a
        if side_b == 0:
            side_b = side_a
        self._length = side_b

    @property
    def width(self):
        return self._width

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, new_len):
        try:
            if new_len <= 0:
                raise ValueError(f"Длина должна быть больше 0. Вы ввели {new_len}")
        except ValueError as e:
            print(e)
        else:
            self._length = new_len

    @width.setter
    def width(self, new_width):
        try:
            if new_width <= 0:
                raise ValueError(f"Ширина должна быть больше 0. Вы ввели {new_width}")
        except ValueError as e:
            print(e)
        else:
            self._width = new_width

    def get_perimeter(self):
        return 2 * (self._width + self._length)

    def get_area(self):
        return self._width * self._length

    def __add__(self, other):
        """
        сложение прямоугольников, складываются периметры исходных прямоугольников
        :return: экземпляр класса "Rectangle" полученный после сложения периметров
        """
        res = self.get_perimeter() + other.get_perimeter()
        try:
            if res > 100:
                raise RectangleAdd('строна нового прямоугольника больше 100')
        except RectangleAdd as e:
            print(e)
        finally:
            return Rectangle(res)

    def __sub__(self, other):
        """
        вычитание прямоугольников, вычитаются периметры исходных прямоугольников
        :return: экземпляр класса "Rectangle" полученный после вычитания периметров
        """
        res = abs(self.get_perimeter() - other.get_perimeter())
        try:
            if res < 100:
                raise RectangleSub('строна нового прямоугольника меньше 100')
        except RectangleSub as e:
            print(e)
        finally:
            return Rectangle(res)

    def __str__(self):
        res = f'Прямоугольник со сторонами {self._width} и {self._length}'
        return res


rectangle1 = Rectangle(7, 11)
print(rectangle1)
rectangle2 = Rectangle(15, 35)
print(rectangle2)
rectangle3 = rectangle1 + rectangle2
print(rectangle3)
rectangle4 = rectangle1 - rectangle2
print(rectangle4)

rectangle1.width = -5
rectangle1.length = -12
print(rectangle1)
