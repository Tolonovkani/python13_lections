# Создайте класс BankAccount, у которого должны быть:
#         переменные объекта
#             balance (со значением 0 по умолчанию)
#             account_id (со значением random.randrange(100000,199999))
#             transactions_history (c пустым словарем)
#         методы
#             withdraw (снять) принимает сумму, которую нужно снять с баланса и возвращает остаток баланса после снятия
#             deposit (положить) принимает сумму, которую нужно положить на баланс и возвращает остаток баланса после пополнения
#         После создания методов и переменных, попробуйте создать счет, пополнить баланс и снять деньги с баланса.
#     В созданный класс BankAccount добавьте методы:
#         receive (принять) который принимает сумму, увеличивает свой баланс, записывает счет отправителя в словарь transactions_history в качестве ключа, и сумму добавляет в список, который является значением. Почему список? Потому что переводов от данного банковского счета может быть много (пока дату перевода не будем записывать).
#         transfer (перевести), который принимает сумму и другой экземпляр класса BankAccount (параметр назовём receiving_account), на который нужно перевести деньги. В результате работы этого метода нужно уменьшить сумму на балансе, вызвать метод receive у receiving_account. Метод должен возвращать остаток денег на балансе после перевода.
#         После реализации этих методов, попробуйте создать несколько счетов, попробуйте совершить несколько денежных переводов.


# import random

# class BankAccount:
#     def __init__(self, balance=0):
#         self.balance = balance
#         self.account_id = random.randrange(100000, 199999)
#         self.transactions_history = {}

#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount
#             return self.balance
#         else:
#             return "Недостаточно средств на счете."

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             return self.balance
#         else:
#             return "Некорректная сумма для пополнения."

#     def receive(self, amount, sender_account_id):
#         if amount > 0:
#             if sender_account_id in self.transactions_history:
#                 self.transactions_history[sender_account_id].append(amount)
#             else:
#                 self.transactions_history[sender_account_id] = [amount]
#             self.balance += amount
#             return self.balance

#     def transfer(self, amount, receiving_account):
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount
#             receiving_account.receive(amount, self.account_id)
#             return self.balance
#         else:
#             return "Недостаточно средств для перевода."

# # Создаем несколько счетов
# account1 = BankAccount()
# account2 = BankAccount()
# account3 = BankAccount()

# # Пополняем и снимаем средства
# account1.deposit(1000)
# account2.deposit(500)
# account1.withdraw(200)
# account3.deposit(1500)

# # Переводим деньги с одного счета на другой
# account1.transfer(100, account2)
# account2.transfer(500, account3)

# # Пополняем и снимаем средства с учетом переводов
# account1.deposit(200)
# account3.withdraw(600)

# # Выводим историю транзакций
# print("История транзакций счета 1:", account1.transactions_history)
# print("История транзакций счета 2:", account2.transactions_history)
# print("История транзакций счета 3:", account3.transactions_history)
# -=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-



# """
# 1) Объявите 3 переменных, запишите в них строку, список и словарь. Затем запишите их в список, и пройдитесь по нему циклом чтобы распечатать длину сразу каждого из объектов.

# my_string = "Пример строки"
# my_list = [1, 2, 3, 4, 5]
# my_dict = {'a': 1, 'b': 2, 'c': 3}

# my_objects = [my_string, my_list, my_dict]

# for obj in my_objects:
#     print(f"Длина объекта: {len(obj)}")


# 2) Создайте классы Dog и Cat с одинаковым методом voice. Для собак он должен печатать "Гав", для кошек "Мяу".
# Объявите для каждого из классов по экземпляру. Затем объявить функцию to_pet(), которая будет принимать животное и вызывать у него метод voice()
# class Dog:
#     def voice(self):
#         print('gav, gav')

# class Cat:
#      def voice(self):
#          print("mia, mia")

# dog = Dog()
# cat = Cat()

# def to_pet(pet):
#     pet.voice()

# to_pet(dog)
# to_pet(cat)

# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-

# 3. Создайте 2 класса: MyInt и MyString, наследуйте MyInt от int, MyString от str. У обоих
# классов переопределите метод, который отвечает за работу с оператором “+”.
# Напишите функцию add_objects(), которая принимает объект одного из 2 типов.
# При сложении объектов класса MyInt должно выдаваться сообщение “Это сложение”, а
# потом идти логика сложения 2 чисел, и выдача результата.
# При конкатенации объектов класса MyString() Должно выдаваться сообщение: “Это
# конкатенация”, а затем логика конкатенации из базового класса и выдача результата.

# class MyInt(int):
#     def __add__(self, other):
#         print("Это сложение")
#         if isinstance(other, MyInt):
#             return MyInt(super(MyInt, self).__add__(other))
#         else:
#             raise TypeError("Unsupported operand type for +")


# class MyString(str):
#     def __add__(self, other):
#         print("Это конкатенация")
#         if isinstance(other, MyString):
#             return MyString(super(MyString, self).__add__(other))
#         else:
#             raise TypeError("Unsupported operand type for +")

# def add_objects(obj1, obj2):
#     if isinstance(obj1, MyInt):
#         return obj1 + obj2
#     elif isinstance(obj1, MyString):
#         return obj1 + obj2
#     else:
#         raise TypeError("Unsupported operand types")

# int1 = MyInt(5)
# int2 = MyInt(10)
# result_int = add_objects(int1, int2)
# print(result_int)

# str1 = MyString("Hello, ")
# str2 = MyString("World!")
# result_str = add_objects(str1, str2)
# print(result_str)

# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-

# 4) Создайте 3 класса: Person, Employee и Student, при этом Employee и Student должны наследоваться от Person. Определите во всех трёх классах метод get_info():
# -для класса Person он должен принимать и возвращать следующее: “Привет, меня зовут Иван Петров”.
# -для класса Employee он должен принимать и возвращать: “Привет, меня зовут Иван Петров, я работаю в компании “Рога и копыта” на должности “директор”.
# -для класса Student должно приниматься и возвращаться: “Привет, меня зовут Иван Петров, я учусь в КГТУ на 3 курсе”.
# Определите функцию get_human_info(), которая будет принимать объект одного из трёх классов, вызывать метод get_info и печатать результат.

# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname

#     def get_info(self):
#         return f"Привет, меня зовут {self.name} {self.surname}"

# class Employee(Person):
#     def __init__(self, name, surname, company, position):
#         super().__init__(name, surname)
#         self.company = company
#         self.position = position

#     def get_info(self):
#         return f"{super().get_info()}, я работаю в компании '{self.company}' на должности '{self.position}'."

# class Student(Person):
#     def __init__(self, name, surname, university, year):
#         super().__init__(name, surname)
#         self.university = university
#         self.year = year

#     def get_info(self):
#         return f"{super().get_info()}, я учусь в '{self.university}' на '{self.year}' курсе."

# def get_human_info(person):
#     print(person.get_info())


# person = Person("Иван", "Петров")
# employee = Employee("Иван", "Петров", "Рога и копыта", "директор")
# student = Student("Иван", "Петров", "КГТУ", "3")

# get_human_info(person)
# get_human_info(employee)
# get_human_info(student)


# $$$$$$$-----$$$$$$$$$$$$$$$-----$$$$$$$$$$$$$$$-----$$$$$$$$$$$$$$$-----$$$$$$$$


# 5) Объявите абстрактный класс геометрических фигур Shape и определите в нём абстрактный метод get_area() для расчёта площади фигуры, которые необходимо переопределить в дочерних классах.

# Затем наследуйте от Shape три класса: Triangle, Square и Circle.
# -треугольник создаётся с заданными основанием и высотой
# -квадрат создаётся с заданной длиной стороны
# -круг создаётся с заданным радиусом
# Переопределите в каждом из классов метод get_area() таким образом, чтобы он рассчитывал площадь для конкретной фигуры.

# Затем создайте от каждого из трёх классов по экземпляру, и вызовите у каждого метод get_area()

# Подсказка: для создания абстрактных классов воспользуйтесь модулем abc

# from abc import ABC, abstractmethod
# import math

# # Определяем абстрактный класс Shape
# class Shape(ABC):
#     @abstractmethod
#     def get_area(self):
#         pass

# # Создаем классы-наследники: Triangle, Square, Circle
# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def get_area(self):
#         return 0.5 * self.base * self.height

# class Square(Shape):
#     def __init__(self, side_length):
#         self.side_length = side_length

#     def get_area(self):
#         return self.side_length * self.side_length

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def get_area(self):
#         return math.pi * self.radius ** 2

# # Создаем экземпляры классов
# triangle = Triangle(4, 6)
# square = Square(5)
# circle = Circle(3)

# # Вызываем метод get_area() для каждой фигуры
# print("Площадь треугольника:", triangle.get_area())
# print("Площадь квадрата:", square.get_area())        
# print("Площадь круга:", circle.get_area()) 