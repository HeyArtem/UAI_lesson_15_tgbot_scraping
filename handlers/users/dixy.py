import requests
import os
from bs4 import BeautifulSoup
import time
import random
import json


'''
Скрапинг сайта 
https://dixy.ru/catalog/

только первую страницу

Парсинг всех страниц в предыдущем проекте
'''

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "Cookie": "BITRIX_SM_PROJECT_GEOLOCATION_PREV_IP=185.94.108.18; BITRIX_SM_PROJECT_GEOLOCATION_REGION=a%3A2%3A%7Bs%3A4%3A%22CITY%22%3Bs%3A12%3A%22%D0%94%D1%80%D1%83%D0%B3%D0%BE%D0%B9%22%3Bs%3A6%3A%22REGION%22%3Bs%3A12%3A%22%D0%94%D1%80%D1%83%D0%B3%D0%BE%D0%B9%22%3B%7D; BITRIX_SM_PROJECT_REGION_ID=21; _ym_uid=166621944326108209; _ym_d=1666219443; _ga=GA1.2.93531338.1666219443; BX_USER_ID=d142b0f88e854573a98c69681f3d4c7d; _gid=GA1.2.1766180313.1666475194; PHPSESSID=4f3f0nhn6rhjtdj4kqueomike2; _ym_isad=1; _ym_visorc=w; _gat_gtag_UA_147107817_1=1"
}

# функция сбора данных
def dixy_data():
    
    # создал объект ссесии
    sess = requests.Session()

    # # запрос   
    # response = sess.get(url='https://dixy.ru/catalog/', headers=headers, verify=False)

    # проверяю и в случае необходимости создаю директорию
    if not os.path.exists('dixy_data'):
        os.mkdir('dixy_data')

    # # сохраняю страницу
    # with open('dixy_data/index.html', 'w') as file:
    #     file.write(response.text)    
    
    # переменна для записи данных в json
    all_data_json_dixy = []
        
    # собираю данные только с первой страницы, т.к. телеграмм не пропускает, по количеству символов
    url_page = f'https://dixy.ru/catalog/?PAGEN_1=1'

    # запрос к странице        
    response = sess.get(url=url_page, headers=headers, verify=False)

    # создаю объект BeautifulSoup
    soup = BeautifulSoup(response.text, 'lxml')

    # нахожу блок с карточками
    product_cards = soup.find_all('div', class_='product-container')

    # собираю информация из карточек  !! забыл собрать ссылку на карточку 
    for card in product_cards:

        try:
            card_name = card.find('div', class_='dixyCatalogItem__hover').text.strip()            
        except Exception as ex:            
            card_name = card.find('div', class_='dixyCatalogItem__title').text.strip()                

        try:
            card_price = card.find('div', class_='dixyCatalogItemPrice__new').text.strip()
        except Exception as ex:
            card_price = "card_price"

        try:
            card_discont = card.find('div', class_='dixyCatalogItemPrice__discount').text.strip().replace('-', '').replace('%', '')
        except Exception as ex:
            card_discont = 'No data'

        # print(f'card_name: {card_name}\ncard_price: {card_price}\ncard_discont(%): {card_discont}\n')

        # собранные данные сохраню в переменную для записи в json
        all_data_json_dixy.append(
            {
                'card_name': card_name,
                'card_price': card_price,
                'card_discont': card_discont,
            }
        )        

    # записываю данные в json
    with open('dixy_data/all_data_dixy.json', 'w') as file:
        json.dump(all_data_json_dixy, file, indent=4, ensure_ascii=False)
    
    return all_data_json_dixy
            

# print('Стартовый принт', dixy_data())
