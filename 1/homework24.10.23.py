# ТЕХНИЧЕСКОЕ ЗАДАНИЕ(сложность: средняя)
# ● Спарсить kolesa.kz, категорию:
# 1.Название всех моделей.
# 2.Цену всех моделей
# 3.Изображение всех моделей
# 4.Краткое описание всех моделей
# 5.Записать все в csv файл

from bs4 import BeautifulSoup
import requests
import csv

url = 'https://auto312.kg/cars.html'

response = requests.get(url).text
soup = BeautifulSoup(response,'lxml')
container = soup.find('div', class_='dj-items-rows')
cars = container.find_all('div', class_='item_row_in')
res = []

for car in cars:
    name = car.find('a', class_='title').text
    price = car.find('div', class_='item_price').text
    img = car.find('a').find('img').get('src')
    image_car = 'https://auto312.kg/' + img
    desc = car.find('div', class_='item_custom_fields').text
    dic = {'name': name, 'price': price, 'image': image_car, 'desc': desc}
    res.append(dic)

def write_to_csv(data: list):
    with open('car.csv', 'w') as file:
        count = 1
        fieldnames = ['№', 'name', 'desc', 'price', 'image']
        writer = csv.DictWriter(file, fieldnames)
        writer.writerow({
            '№': '№', 
            'name': 'Name:', 
            'desc': 'Description:',
            'price': 'Price:', 
            'image': 'Image Url:'
        })
        for car in data:
            writer.writerow({
                '№': count, 
                'name': car['name'], 
                'desc': car['desc'],
                'price': car['price'], 
                'image': car['image']
            })
            count += 1

write_to_csv(res)
