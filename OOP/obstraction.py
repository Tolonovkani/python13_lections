# from abc import ABC,abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def eat(self):
#         pass

#     @abstractmethod
#     def breathe(self):
#         pass

# class Leon(Animal):
#     def eat(self):
#         print('Meal')

#     def breathe(self):
#         print('Lungs')

# obj = Leon()
# obj.eat()
# =================
# Абстракция (Абстрактный класс) - его можно рассматривать как набор методов, который должны быть созданны и реализованы во всех дочерних классах, которые были унаследованны от абстракного класса.

# Абстракный метод - это метод, которого есть обьевление но нет реализации

# from abc import ABC, abstractmethod
# from math import pi

# class Shape(ABC):
#     def __init__(self, name) -> None:
#         self.name = name

#     @abstractmethod
#     def area(self):
#         pass

# class Square(Shape):
#     def __init__(self, lenght) -> None:
#         super().__init__('kvadrat')
#         self.lenght = lenght

#     def area(self):
#         return self.lenght ** 2
    
# class Circle(Shape):
#     def __init__(self, radius) -> None:
#         super().__init__('Circle')
#         self.radius = radius

#     def area(self):
#         return round(pi * self.radius ** 2, 2)
    
# a = Square(4)
# print((a.area()))
# b = Circle(3)
# print(b.area())
# ====================================
# from abc import ABC,abstractmethod

# class ChessPiaes(ABC):
#     # общий метод который будут  исполбзовать все наследники этого класса
#     def draw(self):
#         print('Drew a chess piece')

#     #  абсрактный метод, который необходимо переопределить для каждого дочернего класса
#     @abstractmethod
#     def move(self):
#         pass

# class Queen(ChessPiaes):
#     def move(self):
#         print('The Qeen can move everywhere she wants dioganally, vertically, horizontally')

# class Pawn(ChessPiaes):
#     def move(self):
#         print('The Pawn can move durectly to one or two cells!')


# q = Queen()
# q.draw()
# q.move()

# p = Pawn()
# p.draw()
# p.move()