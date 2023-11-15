from bs4 import BeautifulSoup
import requests
import csv
import re


url = 'https://www.mashina.kg/search/all/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
container = soup.find('div', class_='table-view-list')
cars = container.find_all('div', class_='list-item')

all_url_cars = []
photos_car = []
p = []

description = []
d = []

result = []
for i in cars:
    url_cars = i.find('a').get('href')
    url_cars = 'https://mashina.kg' + url_cars
    all_url_cars.append(url_cars)

for car in all_url_cars:
    response = requests.get(car).text
    soup = BeautifulSoup(response, 'lxml')
    fotos = soup.find('div', class_='fotorama').find_all('a')
    for f in fotos:
        photos = f.get('data-full')
        p.append(photos)
    photos_car.append(p)
    p = []
    desc = soup.find('div', class_='seller-comments').text
    complectat = soup.find('div', class_='configuration').text
    d = [desc + complectat]
    description.append(d)


for el in photos_car:
    for ele in description:
        data = {'Все фото': el, 'Описание': ele}
    result.append(data)
print(result)


with open('car.csv', 'w') as f:
    for i in result:
        for k in i:
            f.write(' '.join(i[k]))