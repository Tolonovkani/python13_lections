# Вы должны спарсить сайт
# https://www.kivano.kg/mobilnye-telefony. Как результат вы должны
# получить:
# 1. Наименование всех телефонов
# 2. Цену каждого продукта(в KGS)
# 3. И ссылка к фотографии
# 4. Все это записать в CSV файл

from bs4 import BeautifulSoup
import requests
import csv

url = 'https://www.kivano.kg/mobilnye-telefony'

response = requests.get(url).text
soup = BeautifulSoup(response,'lxml')
container = soup.find('div', class_='product-index product-index oh')
phone = container.find_all('div', class_='listbox_title oh')
res = []

for phone in phone:
    name = phone.find('a', class_='/product/view/sotovyy-telefon').text
    price =phone.find('div', class_='listbox_price text-center').text
    img = phone.find('div', class_='listbox_price text-center')
    desc = phone.find('div', class_='product_text pull-left')
    dic = {'name': phone, 'price': price, 'img': img, 'desc':desc}.text
    res.append(dic)




def write_price_csv(data: list):
    with open('phone.csv' 'w') as file:
        count =1
        fieldnames = ['#','name','desc','price','imege']
        writer = csv.DictWriter