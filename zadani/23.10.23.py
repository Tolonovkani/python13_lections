from bs4 import BeautifulSoup
import requests
import csv
import lxml

url = 'https://lalafo.kg/'

def parsing_data():

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'lxml')

    container = soup.find('div', class_='main-feed__container css-15re3k2')

    prodogas = container.find_all('article', class_='adTile-wrap')

    result = [] 



    for prodoga in prodogas:         
        price = prodoga.find('p',class_='adTile-price').text.strip()
        img = prodoga.find('img')
        if img is not None:
            img = img.get('data-src')
        desc = prodoga.find('div', class_='adTile-title__wrap').text.strip()
        avatar = prodoga.find('img', class_='userAvatar-photo')
        if avatar is not None:
            avatar = avatar.get('data-src')
        data = {'desc': desc, 'price': price, 'img': img, 'avatar': avatar}
        result.append(data)
        print(data)
    
    write_to_csv(result)


def write_to_csv(data: list):
    with open('prodogas.csv','w') as file:
        count = 1
        fieldnames =['№', 'desc', 'price', 'image','avatar']
        writer = csv.DictWriter(file, fieldnames)
        writer.writerow({
            '№': '№',
            'avatar': 'Avatar:',
            'desc': 'Description:',
            'price': 'Price:',
            'image': 'Image Url:',
        })
        for prodoga in data:
            writer.writerow({
                '№': count,
                'avatar': prodoga['avatar'],
                'desc': prodoga['desc'],
                'price': prodoga['price'],
                'image': prodoga['img'],
            })
            count += 1


parsing_data()



   