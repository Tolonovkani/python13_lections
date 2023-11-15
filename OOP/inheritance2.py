# множественное наследование - это когда класс наследуется от двух или более классов ,порядок наследованиея опредиляется при помощи MRO 

# class Plane:
#     def play_music(self):
#         print('music is playing!')

#     def fly(self):
#         print('We are flying!')

# class Auto:
#     def play_music(self):
#         print('Music is playing on rodio')

#     def ride(self):
#         print('WE are riding on the ground!')

# class Boat:
#     def play_music(self):
#         print('Musuc is playing on karaoke!')

#     def swim(self):
#         print('We are swiming on the sea!')

# class futureAuto(Auto,Boat,Plane):
#     pass

# obj = futureAuto()
# obj.fly()
# obj.swim()
# obj.ride()
# obj.play_music()

# object
# print(object)
# print(dir(object))

# class A:
#     pass

# print(issubclass(A, object))
# --------===----===----===----===----===----===----===----

# Mro glavnai info - (Method resolution order)- механизм для коректного поиска родительских методов.Поиск идет таким оброзом что родительских классов есть предок то поиск идет в ширину другими славами сначала у патомков а потом у общего предка 

# Проблема ромба - когда поиск шел в родительский класс, прежде чем искать  у соседнего общего потомка(решена при помощи MRO)
#  -=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=- -=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-

# class Zero:
#     def say(self):
#         print('class Zero')

# class First(Zero):
#     def say(self):
#         print('class First')

# class Second(Zero):
#     def say(self):
#         print('class Second')

# class Myclass(First,Second):
#     pass   

# obj = Myclass()
# obj.say()
# print(Myclass.mro())
# ------------------------------------
# проблема перекрестного наследования

# class X:
#     pass


# class Y:
#     pass


# class A(X, Y):
#     pass


# class B(Y, X):
#     pass

# class MyMro(type):
#     def mro(cls):
#         return [object, cls, A, B, X,object]

# class Myclass(A, B):
#     pass

# print(Myclass.mro())









