from class_my_excepton import PersonNameException, PersonAgeException


class Person:
    """
    Class создающий персону с возможностью добавления в архив!
    """
    def __init__(self, first_name, last_name, age):
        if len(first_name) < 10:
            self.first_name = first_name
        else:
            raise PersonNameException
        if len(last_name) < 15:
            self.first_name = first_name
        else:
            raise PersonNameException
        self.last_name = last_name
        if 0 < age < 130:
            self.age = age
        else:
            raise PersonAgeException

    def birthday(self):
        """
        Метод позволяющий увеличивать возраст персоны
        :return:
        """
        self.age += 1
        if self.age >= 130:
            raise PersonAgeException

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def person_age(self):
        return self.age

    def writePersonToArchive(self):
        with open('ArchivePerson.txt', 'a', encoding="utf-8") as archive:
            try:
                archive.write(f'Имя - {self.first_name}, Фамилия - {self.last_name}, Возраст - {self.age}')
            except FileNotFoundError:
                print("При записи данных в архив произошла ошибка!")