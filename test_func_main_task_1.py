import pytest
from main_task_1 import filter_list_geo, geo_id, distribution

# Тест на задание №1
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


@pytest.mark.parametrize('lst, country', [(geo_logs, 'Россия')])
def test_filter_list_geo(lst, country):
    assert type(filter_list_geo(lst)) == list
    for item in filter_list_geo(lst):
        for var in item.values():
            assert country in var


# Тест на задание №2
ids1 = {'user1': [213, 213, 213, 15, 213],
        'user2': [54, 54, 119, 119, 119],
        'user3': [213, 98, 98, 35]}

ids2 = {'user3': [218, 218, 100, 15, 213],
        'user4': [54, 54, 119, 119, 13],
        'user5': [213, 98, 98, 100]}

ids3 = {'user6': [2, 2, 25, 15, 21],
        'user7': [54, 54, 1, 1, 3],
        'user8': [2, 9, 9, 100]}


@pytest.mark.parametrize('some_dict', [ids1, ids2, ids3, ])
def test_geo_id(some_dict):
    assert type(geo_id(some_dict)) == list
    assert len(geo_id(some_dict)) == len(set(geo_id(some_dict)))

# Тест на задание №3
queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
]


@pytest.mark.parametrize('some_list', [queries, ])
def test_distribution(some_list):
    for item in some_list:
        assert type(item) == str
    dic = distribution(some_list)
    assert type(dic) == dict
    for var in dic.keys():
        assert type(var) == int
    for var in dic.values():
        assert type(var) == str
