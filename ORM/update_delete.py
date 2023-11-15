from models import Product,Category

# обновления данных

# query = Product.update(price=500).where(Product.title == 'Zara t-shirt')
# print(query)
# query.execute()

# a = Product.update(price=(Product.price + Product.price * 0.5))
# # увелисеваем все товарам цену
# a.execute()
# # -------------------------------------------



# удаления через запрос
# a = Product.delete().where(Product.id == 6)
# a.execute()

# удаления через обьект
# product = Product.get(id=5)
# print(product,product.title)
# product.delete_instance()

# удаления всю 

# a = Product.delete().where(Product.id >= 2)
# print(a)
# a.execute()