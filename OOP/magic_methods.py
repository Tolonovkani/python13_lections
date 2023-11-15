# magic_methods (магическая методы)
# dunder methods (double underscore) -> __init__
# служебные методы 

# магия (фишка) заключаетсмя том что эти методы запускаются без прямого обращения к ним , определенные методы могут отвечать за определенные операторы

# class A(int):
#     def __init__(self) -> None:
#         pass
#     def func(self):
#         pass
# obj = A()
# print(dir(obj))
# obj.func()
# ---------------------------
# dunder methodы сравнения
# __eq__(self,other) -> 5 == 8
                          #5.__eq__(8)
# __ne__ -> !=

# __lt__ -> <

# __gt__ -> >

# __le__ -> <=

# __ge__ -> >=

# __sub__(self,other) -> -
# __mul__ -> * __div__ /

# __nod__ -> %  __floordiv__ -> //

# __add__ -> + __pow__-> **

# class MyClass:
#     def __init__(self, string) -> None:
#         self.string = string

#     def __str__(self) -> str:
#         return self.string
    
#     def __add__(self,other):
#         print('add worked!!')
#         print(self, '***' )
#         print(other, '---')
#         res = self.string + ' ' + other.string
#         return MyClass(res)

# obj1 = MyClass('John')
# obj2 = MyClass('Jamie')
# obj3 = MyClass('Lanister')
# res = obj1 + obj2 + obj3
# print(res, res.string)
# ------------------------------------------
# class Word(str):
#     def __init__(self, word) -> None:
#         self.word = word

#     def __gt__(self, __value: str) -> bool:
#         print('gt сработал')
#         print(self, '!!!!')
#         print(__value, '****')
#         return len(self) > len(__value)
    
# obj1 = Word('Jonh')
# obj2 = Word('Hello word')
# print(obj1 > obj2)
# -=-=-=-=--=-=-=-=--=-=-=-=--=-=-=-=--=-=-=-=-

# дандер методы строкового отбражения обьектов
# __str__ -> для отброжения строки бкоторую будут видеть пользователи
# __repr__ -> строковую информацию о том как создать объект


# print(eval('6*6')) #-> 6*6 -> 36        

# class Base:
#     def __init__(self,string) -> None:
#         self.string = string

#     def __str__(self) -> str:
#         return f'Объект: {self.string}'

#     def __repr__(self) -> str:
#         return 'Base("string")'
    
# user = Base('Hello John')
# print(user)
# a = eval(repr(user))
# print(a)
# ----------------------------------------------
# конструктоор -> __new__(cls)
# инициалзатор -> __init__(self)
# деструктор -> __del__(self)


# class Cifra:
#     def __new__(cls, *args, **kwargs):
#         number = abs(args[0])
#         isinstance = super().__new__(cls)
#         isinstance.number = number
#         return isinstance
#     def __add__(self,other):
#         res = self.number + other.number
#         print(f'Result: {self.number} + {other.number} = {res}')
#         return Cifra(res)

# value1 = Cifra(-177)
# value2 = Cifra(54)
# value3 = Cifra(-7775)
# a = value1 + value2
# value3 + a   
# ------------------------------------
# from random import choice

# class Dog:
#     def sound(self):
#         print('gaw')
# class Cat:
#     def sound(self):
#         print('Mia')

# class Parrot:
#     def sound(self):
#         print('say')

# class Pet:
#     def __new__(cls):
#         other = choice([Dog, Cat, Parrot])
#         instance = super().__new__(other)
#         print(f'I am {type(instance)}')
#         return instance
    
#     def __init__(self) -> None:
#         print('init was never closed!')

# pet = Pet()
# pet.sound()
# -------------------------------------------
# SINGLETON

# class Singleton:
#     _instance = None

#     def __new__(cls):
#         if not cls._instance:
#             cls._instance =super().__new__(cls)
#             return cls._instance
        
#     def __str__(self) -> str:
#         return str(id(self))

# a = Singleton()
# b = Singleton()
# c = Singleton()
# print(a)
# print(b)
# print(c)
# print(a is b)
# print(a is c)
# -----------------------------------------
# class A:
#     def __del__(self):
#         choice  = input('Are tou sure to delete(yes/no):')
#         if choice.lower().strip() == 'yes':
#             print('delaited')
#             del self
#         else:
#             print('Operation denied!')


# obj = A()
# del obj
# print(obj)