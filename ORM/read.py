# import peewee 
# from models import Product,Category

# def get_all_categories():
#     return Category.select()

# def get_all_categories():
#     return Product.select()

# categories = get_all_categories()
# # print(categories)
# print('категории БД:')
# for x in categories:
#     print(x)
#     print(x.title.title())
#     print(x.created_at.strftime('%Y-%m-%d -->> %H:%M:%S'))
#     print()
# --------------------------------
# products = get_all_categories()
# print('Все товары в БД:')
# sum_price = 0
# for x in products:
#     print(f'{x.title}--> {x.price} --> {x.category_id}')
#     print()
#     sum_price += x.price

# print(f'AVG price: {sum_price / len(products)}')

# ---------------------------------
# products = get_all_categories()
# category = int(input('Vedite catigory(6-платья, 7-джинсы, 8-футболки, 9-свитер, 2-обувь):'))
# for c in products:
#     if c.category_id.category_id == category:
#         print(c.title, c.price, c.category_id.title)

# category_name = input("Vedite title category:").lower().strip()
# try:
#     category = Category.get(title=category_name)
#     print(category, category.title)
# except peewee.DoesNotExist:
#     print('Такой катигории нет!')
# else:
#     for product in category.products:
#         print(f'Title: {product.title}, price: {product.price}, category: {product.category_id.title}')