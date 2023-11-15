# полиморфизом - способность метода использоваться в разных типах(классов)
#широко распрастрененное определение "один интерфейс - много реализаций"

# list.pop
# dict.pop
# set.pop

# class Cat:
#     def __init__(self,name, age) -> None:
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f'It\'s cat. Cats name is {self.name}, age: {self.age}')
#     def make_sound(self):
#             print('Mui, mui')



# class Dog:
#     def __init__(self,name, age) -> None:
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f'It\'s dog. Dogs name is {self.name}, age: {self.age}')

#     def make_sound(self):
#         print('Bark,bark')

# obj1 = Cat('Garfild', 5)
# obj1.info()
# obj1.make_sound()

# obj2 = Dog('Pluto', 7)
# obj2.make_sound()
# obj2.info()



# # class Shape:
# #     def __init__(self,name) -> None:
# #         self.name = name

# #     def area(self):
# #         pass

# #     def info(self):
# #         print('Я геометирическая фигура!')

# # class Square(Shape):
# #     def __init__(self, length) -> None:
# #         super().__init__('квадрат')
# #         self.len = length

# #     def area(self):
# #         return self.len ** 2
    
# #     def info(self):
# #         super().info()
# #         print('Все стороны равны и углу все 90 градусов!')

# # class Circle(Shape):
# #     def __init__(self, radius) -> None:
# #         super().__init__('окружуность')
# #         self.r = radius

# #     def area(self):
# #         from math import pi
# #         return round(pi * self.r ** 2,2)
    
# #     def info(self):
# #         return super().info()
# #     print('Диаметр равен двум радиусам!')


# a = Square(8)
# b = Circle(4)

# print(a.info())
# print(a.area())

# print(b.info())
# print(b.area())




























