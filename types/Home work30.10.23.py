 # Напишите класс Subscriber, у которого есть переменные экземпляра:
    #     firstname
    #     lastname
    #     Сделайте так, чтобы метод __repr__ возвращал firstname + lastname
    # Напишите класс Provider, у которого есть:
    #     переменный экземпляра name -- название провайдера
    #     переменный экземпляра subscribers -- список, в котором будут храниться экземпляры класса Subscriber
    #     переменный экземпляра payments -- словарь, ключём которого является экземпляр класса Subscriber, значением является сумма (вещественное число)
    #     метод register_payment, который принимает экземпляр класса Subscriber, и сумму, затем проверяет, есть ли такой экземпляр Subscriber в списке subscribers. 
    #         Если есть, записывает экземпляр в словарь payments в качестве ключа, а сумму в качестве значения
    #         Если нет, выкидывает (raise) ошибку ValueError
    # Напишите класс Terminal, у которого есть
    #     переменная экземпляра amount = 0
    #     переменная экземпляра providers = [ ]
    #     Регистрировать провайдера через метод register, который принимает экземпляр класса Provider и добавляет в providers
    #     Принимать деньги в счет провайдера (pay), который принимает экземпляр класса Provider, экземпляр класса Subscriber и сумму (вещественное число). Внутри метода должен вызываться метод register_payment экземпляра класса Provider. register_payment успешно сработал, то в переменую amount нужно добавить сумму.

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# class Subscriber:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname

#     def __repr__(self):
#         return f"{self.firstname} {self.lastname}"

# class Provider:
#     def __init__(self, name):
#         self.name = name
#         self.subscribers = []
#         self.payments = {}

#     def register_payment(self, subscriber, amount):
#         if subscriber in self.subscribers:
#             self.payments[subscriber] = amount
#         else:
#             raise ValueError("Subscriber not found in the list of subscribers")

# class Terminal:
#     def __init__(self):
#         self.amount = 0
#         self.providers = []

#     def register_provider(self, provider):
#         self.providers.append(provider)

#     def pay(self, provider, subscriber, amount):
#         if provider in self.providers:
#             provider.register_payment(subscriber, amount)
#             self.amount += amount
#         else:
#             raise ValueError("Provider not found in the list of providers")


# # Создаем экземпляры Subscriber
# subscriber1 = Subscriber("John", "Doe")
# subscriber2 = Subscriber("Jane", "Smith")

# # Создаем экземпляр Provider
# provider = Provider("XYZ Internet")

# # Регистрируем Subscriber у Provider
# provider.subscribers.append(subscriber1)
# provider.subscribers.append(subscriber2)

# # Создаем экземпляр Terminal
# terminal = Terminal()

# # Регистрируем Provider в Terminal
# terminal.register_provider(provider)

# # Осуществляем платеж
# terminal.pay(provider, subscriber1, 100.0)

# # Выводим информацию о платеже
# print(f"Amount in Terminal: {terminal.amount}")
# print(f"Payments for {subscriber1}: {provider.payments}")

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=