import peewee
import random
from models import Category,Product


def add_category(name):
    try:
        name = name.lower().strip()
        data = Category(title=name)
        data.save()
        print(f'Сохранили  категорию {name}!')
    except (peewee.IntegrityError,peewee.InternalError):
        print(f'Такая категория {name} уже существует!')

# add_category(' платья ')
# add_category(' джинсы ')
# add_category(' Футболки ')
# add_category(' Свитер ')
# add_category(' обувь ')

def add_product(name, price, category_name):
    try:
        category_id = Category.get(title=category_name.lower().strip())
    except peewee.DoesNotExist:
        category_id = None

    if category_id:
        data = Product(title=name, price=price, category_id=category_id)
        data.save()
        print(f'Сохранили товар {name}!')
    else:
        print(f'Категории {category_name} не существует!')

# add_product('Zara t-shirt', 300, 'Футболки')
# add_product('Supreme t-shirt', 350, 'Футболки')
# add_product('Polo t-shirt', 200, 'Футболки')
# add_product('Aygen58 t-shirt', 150, 'платья ')
# add_product('lewys', 500, 'джинсы ')
# add_product('Nike Air Jordan', 1500, 'обувь ')
# add_product('Polo', 700, 'свитеры ')

# add_category('cars')
# add_category('telefony')

# with open ('files/telefon.txt', 'r') as file:
#     ls = file.readlines()
#     print(ls)
#     for x in ls:
#         name = x.strip()
#         price = random.randint(100,200)
#         add_product(name, price, 'telefony')