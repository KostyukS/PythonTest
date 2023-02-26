from pprint import pprint

# Задание 1
# Дан список с визитами по городам и странам.
# Напишите код, который возвращает отфильтрованный список geo_logs, содержащий только визиты из России."

geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]


def filter_list_geo(some_list):
    geo_copy = []
    for item in some_list:
        for key in item.keys():
            for val in item[key]:
                if 'Россия' in val:
                    dic = dict()
                    dic[key] = item[key]
                    geo_copy.append(dic)
    return geo_copy


# Задание 2
# Выведите на экран все уникальные гео-ID из значений словаря ids.
# Т.е. список вида [213, 15, 54, 119, 98, 35]

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}


def geo_id(some_dict):
    list_ids = []
    for item in some_dict.values():
        list_ids += item
    unic_id = set(list_ids)
    return list(unic_id)


# Задание 3
# Дан список поисковых запросов.
# Получить распределение количества слов в них. Т.е. поисковых запросов из одного - слова 5%,
# из двух - 7%, из трех - 3% и т.д.

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
]


def distribution(some_list):
    num_word = []
    num_dict = {}
    for str in some_list:
        num_word.append(len(str.split()))
    unic = list(set(num_word))
    for item in unic:
        dist = 100 / len(num_word) * num_word.count(item)
        num_dict[item] = f'{round(dist, 2)} %'
    return num_dict


if __name__ == '__main__':
    print('Задание №1')
    pprint(filter_list_geo(geo_logs))
    print('=' * 40)
    print('Задание №2')
    print(geo_id(ids))
    print('=' * 40)
    print('Задание №3')
    print(distribution(queries))
