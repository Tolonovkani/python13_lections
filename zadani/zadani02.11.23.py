# 1.
# Вам дан список со словарями, сериализуйте этот список в json-строку
# import json

# list = [
#     {'key1': 'HI','key2': 'Hello'},
#     {'key3': 'salam', 'key4': 'Privet'}
#     ]

# with open('data-test.json', 'w') as file:
#     json.dump(list, file, indent=4)

# 2.
# Вам дана json-строка, десериализуйте ее. 
# Выведите названия тех продуктов, рейтинг которых больше 4

# import json
# with open('data-test.json', 'r') as file:
#     data = json.load(file)
#     for i in data:
#         if i["rating"] >= 4:
#             print(i)

# ===========================
# 3.
# Вам дан файл db.json. Десериализуйте данные с него. 
# Добавьте в каждый продукт новую пару ("description":"..."). 
# Запишите измененные 
# данные в файл new_db.json

# import json

# with open('db.json', 'r') as file:
#     data = json.load(file)

# for product in data:
#     product['description'] = 'hello my friend'

# with open('new_db.json', 'w') as new_file:
#     json.dump(data, new_file,indent=4)

# print('данные успешшно обновлены и сохронены в new_db.json')

# 4.
# Удалите из файла new-db.json продукт с id 3.

# import json

# with open('new_db.json', 'r') as file:
#     data = json.load(file)

# product_id_to_delete = 3


# new_products = [product for product in data if product['id'] != product_id_to_delete]
# data = new_products


# with open('new_db.json', 'w') as new_file:
#     json.dump(data, new_file, indent=4)

# print(f"Продукт с id {product_id_to_delete} успешно удален из new_db.json")


# 5.
# Напишите функцию, которая будет запрашивать id, title, description, price, rating и добавлять этот продукт в new_db.json
# import json

# def fun(id, title, description, price, rating):
#     a = {'id': id, 'title': title, 'description': description, 'price': price, 'rating': rating}
#     return a
# a = fun(1, 'qwerty', 'qwerty', 123, 8)
# with open('new_db.json', 'w') as file:
#     json.dump(a, file, indent=4)

# 6.
# Напишите функцию, которая будет принимать id продукта
# если такого продукта нет в new_db.json, функция выводит ошибку
# если такой продукт есть, то запрашивается id, title, description, price, rating и продукт должен обновиться в new_db.json

# import json

# def update_product_info(product_id):
#     # Открываем файл new_db.json для чтения
#     with open('new_db.json', 'r') as file:
#         data = json.load(file)

#     # Проверяем, есть ли продукт с указанным ID
#     if product_id not in data:
#         print(f"Продукт с ID {product_id} не найден в базе данных.")
#         return

#     # Запрашиваем новые данные о продукте
#     new_id = input("Введите новый ID продукта: ")
#     new_title = input("Введите новое название продукта: ")
#     new_description = input("Введите новое описание продукта: ")
#     new_price = float(input("Введите новую цену продукта: "))
#     new_rating = float(input("Введите новый рейтинг продукта: "))

#     # Обновляем информацию о продукте в базе данных
#     data[product_id] = {
#         "id": new_id,
#         "title": new_title,
#         "description": new_description,
#         "price": new_price,
#         "rating": new_rating
#     }

#     # Записываем обновленные данные обратно в файл
#     with open('new_db.json', 'w') as file:
#         json.dump(data, file, indent=4)

#     print(f"Продукт с ID {product_id} успешно обновлен.")

# # Пример использования
# product_id = input("Введите ID продукта, который вы хотите обновить: ")
# update_product_info(product_id)



# 7.
# Напишите функцию, которая будет вытаскивать все продукты из new_db.json и выводить отсортированный список с продуктами по рейтингу (в порядке убывания)


# 8.
# Напишите функцию, которая принимает часть названия и выводит список из всех продуктов из new_db.json в названиях которых будет находится эта часть названия


# 9.
# Напишите функцию, которая принимает цену и выводит список из всех продуктов из new_db.json цена которых больше или равна заданной



# 10.
# Напишите функцию, которая принимает список из продуктов
# эти продукты должны будут добавиться в new_db.json
# если продукт с таким же id уже есть в new_db.json, то он не добавляется