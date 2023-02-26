import requests
from pprint import pprint

token = 'AQAAAAATeViuAADLWyqJ3Qq4ykievdqZkK0qGd4'
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'OAuth {token}'
}
url = 'https://cloud-api.yandex.net/v1/disk/resources'


# Функция создающая папку и проверяющая её наличие на диске
def create_folder(name_folder):
    params = {'path': name_folder}
    requests.put(url, headers=headers, params=params)
    res = requests.get(url, headers=headers, params=params)
    if res:
        print(f'Папка {name_folder} создана')
    return res


# Функция удаляющая папку
def del_folder(name_folder):
    params = {'path': name_folder}
    res = requests.delete(url, headers=headers, params=params)
    return res


if __name__ == '__main__':
    create_folder('Some_folder')
    print('=' * 40)
