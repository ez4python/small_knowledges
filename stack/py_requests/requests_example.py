import json

import requests
from bs4 import BeautifulSoup


def parse():
    main_url = 'https://alijahon.uz'
    url = 'https://alijahon.uz/category'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    product = soup.find('div', class_='col-6 mb-3 col-md-6 col-lg-4')
    product_title = product.find('a', {'class': 'text-dark'}).text
    product_photo_url = product.find('img', {'class': 'img-fluid rounded-top'}).get('src')
    product_url = product.find('a', {'class': 'd-block'}).get('href')
    price = product.find('h5', {'class': 'fs-md-2 text-warning mb-0 d-flex align-items-center mb-2'}).text.strip()
    category = product.find('a', {'class': 'text-500'})
    category_name = category.text
    category_url = category.get('href')

    data = {
        'product': {
            'title': product_title,
            'photo_url': main_url + product_photo_url,
            'url': main_url + product_url,
            'price': price,
            'category': {
                'name': category_name,
                'url': main_url + category_url
            }
        }
    }

    data = json.dumps(data, indent=4)
    return data


if __name__ == '__main__':
    print(parse())
