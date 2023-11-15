# OOP - object oriented programming

# целью создание было связать данные с функциями которые управляют этими данными

# класс это описание того как выглядить объект, то есть в классах мы записываем какимы данными и функциямы будет обладать объект

# объект - сущность которую мы создаем от класса у каждого объекта  есть собственные данные

# аттрибуты - обычные переменные внутри класса

#  методы -функции внутри класса
# ------------------------------------------------

# class Human:
#     age = 0

#     def __init__(self,first_name,last_name,job,citizenship):
#         self.name = first_name + ' ' + last_name
        
#         self.job = job
#         self.citizen = citizenship

#     def show_info(self):
#         return f'Name: {self.name}, Age: {self.age}, job: {self.job}, citisenship: {self.citizen}'
    
# john = Human('John', 'Snow', 'King of North', 'Northener')
# james = Human('James', 'Kirk', 'programmer', 'USA')

# print(john.show_info())
# print(james.show_info())
# james.age = 24
# john.age = 54
# print(john.show_info())
# print(james.show_info())
# ===========================================

# class Dog:
#     age = 0
#     ushi = True

#     def __init__(self, name: str, color: str) -> None:
#         '''инициализатор именно здесь создаются аттрибутты обьекта'''

#         self.name = name 
#         self.color = color

#     def bark(self):
#         print(f'{self.name} лает!')

#     def show_info(self):
#         print(f'Name: {self.name}, Age: {self.age}, Color: {self.color}, ushi: {self.ushi}')

# rex = Dog('Rex', "black")
# pluto = Dog(color='brown', name='Pluto')
# aktosh = Dog('Aktosh', 'gray')

# rex.show_info()
# pluto.show_info()
# aktosh.show_info()

# rex.age = 2
# pluto.age = 5
# aktosh.age = 1
# aktosh.ushi = False

# rex.bark()
# pluto.bark()
# aktosh.bark()


# rex.show_info()
# pluto.show_info()
# aktosh.show_info()


# class Humen():
#     def __init__(self,name) -> None:
#         self.name = name
#         self.golod = 100

#     def walk(self):
#         print(f'{self.name} walking around!')
#         self.golod += 30

#     def work(self):
#         print(f'{self.name} rabota raboteat!')
#         self.golod += 50

#     def eat(self,meal, finish=True):
#         print(f'{self.name} eat {meal}!')
#         if finish:
#             self.golod -= 60 if finish else 30

#     def info(self):
#         print(f'{self.name} ---> {self.golod}')  
# obj = Humen('Ala')
# obj.info()
# obj.eat('kruasan')
# obj.eat('sandwitch', finish=False)
# obj.info()
# obj.walk()
# obj.work()
# obj.info()
# obj.eat('burger')
# obj.eat('fri')
# obj.eat('pepsi', finish=False)
# obj.info()
# ------------------------------------------------

# class Car:
#     def __init__(self,brand, model,color) -> None:
#         self.brand = brand
#         self.model = model
#         self.color = color

#     def show_info(self):
#         return f'{self.brand} {self.model} --> {self.color}'
    
#     def __str__(self) -> str:
#         return f'{self.brand} {self.model} --> {self.color}'
    
# obj = Car('Mersedes', 's-class', 'black')
# obj2 = Car('Bmw', 'x5', 'blue')
# obj3 = Car('lexus', 'lx', 'white')


# print(obj.show_info())
# print(obj2.show_info())
# print(obj3.show_info())

# print(obj)
# print(obj2)
# print(obj3)
# ------------------------------

# import random

# class Sniper:
#     health = 100

#     def __init__(self,name) -> None:
#         self.name = name

#     def shoot(self,other: 'Sniper'):
#         other.health -= 20 
#         print(f'Атаковал {self}, y {other} осталось {other.health}!')

#     def __str__(self) -> str:
#         return f'{self.name}'
# Sniper1 =Sniper ('Johne Wick')
# Sniper2 = Sniper('James Bond')

# while Sniper1.health and Sniper2.health:
#     choice = random.randint(1, 2)
#     Sniper1.shoot(Sniper2) if choice == 1 else Sniper2.shoot(Sniper1)

# print(f'{Sniper1 if Sniper1.health else Sniper2} won the game!!!')






