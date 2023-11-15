# Инкапсуляция 
# 1. Языковая конструксия которая помогает связать данные с методоми для их оброботки и управления (связ между данными и методами которые ползуются ими )(класс капсула)

# 2. Механизым сокрития, при поомощи которого можно ограничить доступ одного компонента к другому компоненту  

#  Инкапсуляция как механизм сокрытия
# 3 уровня сокрытия данных:
    # 1. Публичный(public)- number,print_number
    # 2. Защищенный(_protected) - _number
    # 3. Приватный (__private) - __numberсокрытия

# class Car:
#     _country = "Germany"
#     __motor = "Turbo diesel"

#     def __init__(self) -> None:
#         self.marka = "Mersedes-Bens" # Public
#         self._model = "w140" # _protected 
#         self.__color = "gray" # __private

# obj = Car()
# print(dir(obj))
# print(obj._country)
# print(obj._model)
# print(obj._Car__motor)
# -------------------------------------------

# class Phone:
#     username = "John"
#     _caller = "Jamie"
#     __count_of_calls = 15


#     def call(self):
#         print(f'{self._caller} Звонит Вам!')
#         choice = input('Взять трубку (yes/no): ').lower().strip()
#         self._turn_on() if choice == "yes" else print('сбросили трубку')
       

#     def __increment_callls(self):
#         self.__count_of_calls += 1

#     def _turn_on(self):
#         self.__increment_callls()
#         print("Alo!")
#         print(f'Count of calls with {self._caller}: {self.__count_of_calls}')


# phone = Phone()
# print(phone.username)
# phone.call()
# phone.call()
# phone.call()
# phone.call()
# ----------------------------------------

# class Person:
#     def __init__(self,name,age) -> None:
#         self._name = name
#         self._age = age
#     def display_info(self):
#         print(f'My name is {self._name} and i am {self._age} years old!')

#     def set_name(self,name):
#         if isinstance(name, str):
#             self._name = name
#         else:
#             try:
#                 self._name 
#             except AttributeError:
#                 self._name = None
#             print('Name must be str object!')

#     def set_age(self,age):
#         if isinstance(age, int) and 0 < age < 200:
#             self._age = age
#         else:
#             try:
#                 self._age
#             except AttributeError:
#                 self._age = None
#             print('Age must be int object!')


# obj = Person(55 , 24)
# obj.display_info()
# obj.set_name("Jamie")
# obj.set_age(28)
# obj.display_info()
# obj.set_name(55) 
# obj.set_age(28)
# obj.set_age(28)
# obj.display_info()
#  ---------------------------------------------------
# getter & setter
# Они нужны чтобы избежать прямого оброщения к сокрытом атрибутам
# При этом можно добавить логику валидация (проверки) данных которые будут устоновлены в атрибуты и тд


# Антоция свойств(@property(getter setter))

# class Person:
#     def __init__(self) -> None:
#         self.__name = None
#         self.__age = None
#     @property # getter
#     def name(self):
#         return self.__name
#     @property # getter
#     def age(self):
#         return self.__age
    
#     @name.setter
#     def name(self, other):
#         if not isinstance(other, str): print('name must be str object!')
#         else: self.__name = other

#     @age.setter
#     def age(self, other):
#         if isinstance(other,int) and 0 < other < 200:
#             self.__age = other
#         else: print('Age must be int object!')



    

# obj = Person()
# print(obj.name, obj.age)
# obj.name = 'John'
# obj.age = 24
# print(obj.name, obj.age)
# obj.name = 55 
# obj.age = (1, 2, 3, 4)
# print(obj.name, obj.age)
