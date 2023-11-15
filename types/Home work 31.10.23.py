# Ниже представлены связанные задачи. Цель: создать симуляцию университета. Обратите внимание на методы add_department и add_student. Подумайте, как решить проблему перезаписи существующих в словаре данных.

#     Создайте класс University. В конструкторе создайте переменную экземпляра name, куда записывается переданный аргумент university_name.
#     Создайте переменную класса departments, у которого значение по умолчанию -- пустой словарь
#     Создайте метод add_department, у которого параметр название факультета. Метод должен записать в словарь departments название факультета, а в качестве значения -- пустой список
#     Создайте класс Student, в конструкторе которого записывается firstname, lastname студента. Т.е. при создании экземпляра должны быть переданы имя и фамилия студента.
#     Создайте метод add_student с параметрами название факультета и объект студент -- экземпляр класса Student. Метод должен записать в словарь departments студента в соответствующий факультет.
#     Создайте экземпляр университета. Создайте нескольких студентов. Добавьте факультеты. Добавьте студентов в факультеты.

class Student:
    def __init__(self, firstname, lastname):
        self.name = firstname + " " + lastname

 
class University:
    def __init__(self, university_name):
        self.name = university_name
        self.departments = {}  

    def add_department(self, department_name):
        if department_name not in self.departments:
            self.departments[department_name] = [] 

    def add_student(self, department_name, student):
        if isinstance(student, Student):
            if department_name in self.departments:
                self.departments[department_name].append(student.name)
            else:
                raise KeyError('Такого факультета нет!')
        else:
            raise Exception('Такого студента нет!')
        
a = Student('Алтай', 'Байтереков')
        
kgma = University('КГМА')
kgma.add_department('Фармация')
kgma.add_department('Фармация')


kgma.add_student('Фармация', a)
kgma.add_student('Фармация', a)

print(kgma.departments)