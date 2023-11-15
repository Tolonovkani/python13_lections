
from bs4 import BeautifulSoup
import requests
import csv

url = 'https://www.mashina.kg/search/all/'

def parsing_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    container = soup.find('div', class_='table-view-list')
    cars = container.find_all('div', class_='list-item')
    result = []

    for car in cars:
        name = car.find('h2', class_='name').text.strip()
        try:
            img = car.find('img', class_='lazy-image').get('data-src')
        except AttributeError:
            img = 'No Image!'
        price = car.find('div', class_='block price').find('p').find('strong').text
        desc = ' '.join(car.find('div', class_='item-info-wrapper').text.split())
        data = {'title': name, 'desc': desc, 'price': price, 'img': img}
        result.append(data)
        # print(data)
    
    write_to_csv(result)

def get_last_page(url):
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')
    pages = soup.find('ul', class_='pagination').find_all('a',class_='page-link')
    last_page = pages[-1].get('data-page')
    return int (last_page)


def prepare_csv():
    with open('cars.csv','w') as file:
        fieldnames = ['№', 'name', 'desc', 'price', 'image']
        writer = csv.DictWriter(file, fieldnames)
        writer.writerow({
            '№': '№',
            'name': 'Name:',
            'desc': 'Description:',
            'price': 'Price:',
            'image': 'Image Url:',
        })





def write_to_csv(data: list):
    with open('cars.csv', 'a') as file:
        global count
        fieldnames = ['№', 'name', 'desc', 'price', 'image']
        writer = csv.DictWriter(file, fieldnames)
        for car in data:
            writer.writerow({
                '№': count,
                'name': car['title'],
                'desc': car['desc'],
                'price': car['price'],
                'image': car['img'],
            })
            count += 1

prepare_csv()
lasat_page = get_last_page(url)
i = 1
count = 1
while True:

    page_url = f'https://www.mashina.kg/search/all/?page={i}'
    parsing_data(page_url)
    print(f'Спарсили {i}/{lasat_page} страницу!')
    if i == lasat_page:
        print('parsingfinished')
        break
    i +=1