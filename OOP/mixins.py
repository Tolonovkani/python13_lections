# Mixins
# Миксины - классы которые используются для наследованния и передачи дочерным классам определенных методов, но от них создаются обьекты
# для чего:
# 1. Вы хотите предоставить множества доп методов для классов
# 2. Вы хотите использовать один конкретний метод во множестве разных кдассов

# class EngineMixin:
#     def start_engline(self):
#         print('started engine')

# class RadioMixin:
#     def play_radio(self):
#         print('music is playing')

# class Auto(EngineMixin, RadioMixin):
#     pass

# class Plane(EngineMixin, RadioMixin):
#     pass

# class Smartphone(EngineMixin, RadioMixin):
#     pass

# class Train(EngineMixin, RadioMixin):
#     pass
# =================================================

class FlyMixin:
    def fly(self):
        print('I can fly!')

class WalkMixin:
    def walk(self):
        print('I can walk!')

class SwimMaxin:
    def swim(self):
        print('I can swim!')

class Human(WalkMixin, SwimMaxin):
    name = 'human'

    def talk():
        print('I can talk')

class Fish(SwimMaxin):
    name = 'fish'

class Volans(SwimMaxin,FlyMixin):
    name = 'volan'

class Duck(SwimMaxin, FlyMixin):
    name = 'duck'

obj = Human()
obj.walk()
obj.swim()
