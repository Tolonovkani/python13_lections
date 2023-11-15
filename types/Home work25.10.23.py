# Автомобиль: создайте класс с именем Car. Метод __init__ () класса Car должен содержать три атрибута: brand, year и color. Создайте метод get_auto(), который выводит информацию об автомобиле, и метод get_year, который выводит возраст авто .
# Добавьте атрибут horsepower, который равен 85.

# Напишите метод add_horsepower, который всем машинам будет добавлять по 20 л/с, а машинам Mers, Bmw, Poshe по 40 л/с

# Создайте на основе своего класса экземпляр с именем bmw . Выведите три атрибута по отдельности, затем вызовите все методы.

# Два авто: начните с класса из вышеописанного упражнения. Создайте 2 разных экземпляра, вызовите для каждого экземпляра метод get_auto


# class Car:
    

#     def __init__(self,brand,color,year) -> None:
#         self.brand = brand
#         self.color = color
#         self.year = year
#         self.horsepower = 85

#     def get_auto(self):
#         print(f'марка авто {self.brand} цвет авто {self.color} год  {self.year} авто')

#     def get_year(self,year1) -> int:
#         return f'{year1 - int(self.year)} лет'
    
#     def add_horsepower(self):
#         if self.brand in ['mersedes','bmw','porshe']:
#             self.horsepower += 40
#         else:
#             self.horsepower += 20
#         return f'{self.horsepower} мощность'

# bmw = Car('mersedes', 'black', '2015')
# bmw.get_auto()
# print(bmw.get_year(2023))
# print(bmw.add_horsepower())

# llll = Car('lexus', 'red', '2005')
# llll.get_auto()
# print(llll.get_year(2023))
# print(llll.add_horsepower())

# kkkk = Car('bmw', 'black', '2023')
# kkkk.get_auto()
# print(kkkk.get_year(2023))
# print(kkkk.add_horsepower())

# print(bmw.brand)
# print(bmw.color)
# print(bmw.year)
# -------------------------------------------

# Студенты: создайте класс с именем Student. Создайте атрибуты name, age, course. Напишите метод get_student(), который выводит сводку с информацией о студенте . Создайте еще один метод get_birth_year() для вывода информации о годе рождения студента.

# Создайте несколько экземпляров, представляющих разных студентов. Вызовите оба метода для каждого студента.

# class Student:
    
#     def __init__(self,name,age,course) -> None:
#         self.name = name
#         self.age = age
#         self.course =course

#     def get_student(self):
#         return f'имя студента {self.name} возраст {self.age} название курса {self.course}'

#     def det_birth_year(self,year) -> int:
#         return f'{year - self.age} года рождение'
    
# student = Student('Алмаз', 12,  'Салам')
# print(student.get_student())
# print(student.det_birth_year(2023))
        
 