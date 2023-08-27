class PersonException(Exception):
    pass


class PersonNameException(PersonException):
    """
    Class проверяющий длинну имени или фамиллии на установленные длины
    """
    def __init__(self):
        pass

    def __str__(self):
        return f'Имя и Фамилия не могут превышать заданный лимит и могуть быть только в строковом представлении'


class PersonAgeException(PersonException):
    """
    Class проверяющий возраст, Возраст не может быть отритцательным числом и не может привышать определённый лимит
    """
    def __init__(self):
        pass

    def __str__(self):
        return f'Возраст не может быть отритцательным числом и не может превышать отметку 130 лет!'