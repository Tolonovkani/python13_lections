# Создайте класс, сохраняющий каждый экземпляр в переменную класса all_contacts = [ ]. В инициализаторе класса должны быть параметры name, lastname, phone_number. Подсказка: подумайте о self.

# Создайте субкласс Friend, у которого должен быть метод play_football_with_me()

# Создайте класс ContactList, который должен наследоваться от встроенного класса list. В нем должен быть реализован метод search_by_name, который должен принимать имя, и возвращать список всех совпадений. Замените all_contacts = [ ] на all_contacts = ContactList(). Создайте несколько контактов, используйте метод search_by_name.



# class Contact:
#     all_contacts =[]
#     def __init__(self,name, lastname, phone_number) -> None:
#         self.name = name
#         self.lastname = lastname
#         self.phone_number = phone_number
#         self.all_contacts.append(self)


# class Friend(Contact):
#     def play_footbal_with_me(self):
#         print(f'{self.name} играют са мной футбол!')

# class Contactlist(list):
#     def search_by_name(self,name):
#         matching_cotacts = []
#         for contact in self:
#             if contact.name == name:
#                 matching_cotacts.append(contact)
#         return matching_cotacts
    
# a1 = Contact('Aiba', 'Aibekov', '777-777-777')
# a2 = Contact('Kanybek', 'Kanybekov', '555-555-555')
# a3 = Contact('Azamat', 'Azamatov', '222-222-222')

# all_contacts = Contactlist(Contact.all_contacts)

# name_to_search = 'Kanybek'
# matching_contacts = all_contacts.search_by_name(name_to_search)

# if matching_contacts:
#     print(f'Совпадающие имя контакта {name_to_search}!')
#     for contact in matching_contacts:
#         print(f'{contact.name} {contact.lastname}: {contact.phone_number}')
# else:
#     print(f'Контакт с иминем {name_to_search} не найдено!')
# \/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/

# 2)Реализуйте родительский класс Publication, конструктор которого принимает name, date, pages, library, type

# Создайте субкласс Book. В конструктор родительского класса должен передавать type=’book’

# Создайте субкласс Magazine. В конструктор родительского класса должен передавать type=’magazine’

# Создайте субкласс Newspaper. В конструктор родительского класса должен передавать type=’newspaper’

# В классе Publication создайте метод name, date, pages, library, type который будет возвращать первые_2_буквы_библиотеки_тип_первые_2_буквы_названия_количество_страниц_дата_без_точек
        
# class Publication:
#     def __init__(self, name, date, pages, library,type) -> None:
#         self.name = name
#         self.date = date
#         self.pages = pages
#         self.library = library
#         self.type = type

#     def get_code_in_library(self):
#         librery_code = self.library [:2]
#         type_code = self.type
#         name_code = self.name [:2]
#         pages_code = str(self.pages)
#         date_cod = self.date.replace('.','')
#         return f"{librery_code}_{type_code}_{name_code}_{pages_code}_{date_cod}"
    
# class Book(Publication):
#     def __init__(self, name, date, pages, library, type) -> None:
#         type='book'
#         super().__init__(name, date, pages, library, type)

# class Magazine(Publication):
#     def __init__(self, name, date, pages, library, type) -> None:
#         type='magazine'
#         super().__init__(name, date, pages, library, type)

# class Newspaper(Publication):
#     def __init__(self, name, date, pages, library, type) -> None:
#         type='newspaper'
#         super().__init__(name, date, pages, library, type)

# book = Book('Книжный дом', '2023.10.23', 250, 'Lib1', type)
# magazine = Magazine('Лучшие книги', '2012.05.22', 300, 'Lib2',type)
# newspaper = Newspaper('Интересный дом', '2005.01.01', 400,  'Lib3', type)

# print(book.get_code_in_library())
# print(magazine.get_code_in_library())
# print(newspaper.get_code_in_library())

# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/

# Создайте класс Weight (Вес).
#         Создайте метод init() и определите внутри него три динамических атрибута: gram (граммы, целочисленное значение), kilogram (килограммы, целочисленное значение) и centner (центнер, целочисленное значение) . Свои начальные значения они получают из параметров метода init (). Если не указывать значения gram и kilogram, то по умолчанию их значение равна 0.
#         Напишите магический метод str () в котором будет возвращаться информация: «Вес .. центнеров, .. кг, .. гр».
#         Напишите методы прибавления add и убавления sub для данного класса
#         Напишите методы сравнения двух экземпляров класса (eq, gt, le и т.д.)
#     Создайте отдельный файл для проверки класса Weight. В данном файле проверьте:
#         Результат прибавления одного экземпляра класса на другой
#         Результат убавления одного экземпляра класса от другой
#         И все сравнения двух экземпляров класса (eq, gt, le и т.д.

# class Weight:
#     def __init__(self,center, gram = 0,kilogram = 0) -> None:
#         self.gram = gram 
#         self.kilogram = kilogram
#         self.center = center
#     def __str__(self) -> str:
#         return f'«Вес:{self.center} центнеров, {self.kilogram} кг, {self.gram} гр».'
#     def __add__ (self,other):
#         return f'{self.center + other.center}{self.kilogram + other.kilogram}{self.gram + other.gram}'
#     def __sub__(self,other):
#         return f'{self.center - other.center}{self.kilogram - other.kilogram}{self.gram - other.gram}'
        

#     def __eq__(self,other):
#         a = f"{self.center}{self.kilogram}{self.gram}"
#         b = f"{other.center}{other.kilogram}{other.gram}"
#         if int(a) == int(b):
#             return True
#         else:
#             return False

#     def __gt__(self,other):
#         a = f"{self.center}{self.kilogram}{self.gram}"
#         b = f"{other.center}{other.kilogram}{other.gram}"
#         if int(a) > int(b):
#             return True
#         else:
#             return False
        
#     def __gt__(self,other):
#         a = f"{self.center}{self.kilogram}{self.gram}"
#         b = f"{other.center}{other.kilogram}{other.gram}"
#         if int(a) < int(b):
#             return True
#         else:
#             return False

#     def __ge__(self,other):
#         a = f"{self.center}{self.kilogram}{self.gram}"
#         b = f"{other.center}{other.kilogram}{other.gram}"
#         if int(a) >= int(b):
#             return True
#         else:
#             return False

#     def __le__(self,other):
#         a = f"{self.center}{self.kilogram}{self.gram}"
#         b = f"{other.center}{other.kilogram}{other.gram}"
#         if int(a) <= int(b):
#             return True
#         else:
#             return False
        
# a = Weight(55, 8, 5)
# b = Weight(66, 8, 8)
# print(a)
# print(b)
# print(a == b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)
 
    