from pandas_ods_reader import read_ods
import random

from main import parser

ods_path = "./Cities_v4.ods"

with open("./cities.txt", encoding='utf-8') as file:
    cities_title = [row.strip() for row in file]

cities = read_ods(ods_path, 1, headers=True)
cities.index = cities.index + 1


# print(cities)


def full_list():
    print('\nСписок доступных городов:')
    for city in cities_title:
        print(city)


def random_city():
    print('\n', cities.iloc[random.randint(0, 30)], '\n')


def find_city(title):
    num_cities = cities.shape[0]
    for i in range(num_cities):

        if cities.iloc[i]['Город'].lower() == title.lower():
            print('\n', cities.iloc[i], '\n')
            return

    return -1


def output_all_cities(res_cities):
    for i in (res_cities):
        print('\n', i, '\n')
        print('---------------------\n')


def output_cities(phrase, selected_attributes):
    print(phrase, selected_attributes)
    count = 0
    num_cities = cities.shape[0]
    if (selected_attributes == 'Цена'):
        phrase_word = phrase[0]
        for i in range(num_cities):
            if phrase_word == "дешево":
                if cities.iloc[i][selected_attributes] < 6000:
                    count = 1
                    print('\n', cities.iloc[i], '\n')
                    print('---------------------\n')
            elif phrase_word == "нормально":
                if cities.iloc[i][selected_attributes] >= 6000 and cities.iloc[i][selected_attributes] < 6800:
                    count = 1
                    print('\n', cities.iloc[i], '\n')
                    print('---------------------\n')

            elif phrase_word == "доступно":
                if cities.iloc[i][selected_attributes] >= 6800 and cities.iloc[i][selected_attributes] <= 7200:
                    count = 1
                    print('\n', cities.iloc[i], '\n')
                    print('---------------------\n')

            elif phrase_word == "комфортно":
                if cities.iloc[i][selected_attributes] >= 7200 and cities.iloc[i][selected_attributes] < 7800:
                    count = 1
                    print('\n', cities.iloc[i], '\n')
                    print('---------------------\n')

            elif phrase_word == "дорого":
                if cities.iloc[i][selected_attributes] >= 7800:
                    count = 1
                    print('\n', cities.iloc[i], '\n')
                    print('---------------------\n')
    else:

        for i in range(num_cities):
            if (cities.iloc[i][selected_attributes] and
                    cities.iloc[i][selected_attributes].lower() in set(phrase)):
                count = 1
                print('\n', cities.iloc[i], '\n')
                print('---------------------\n')

    if count == 0:
        print('\nТакого не существует...')


def text_values_city(phrase, tmp_cities, text_fields):
    res_cities = []

    intersection = set(phrase) & text_fields

    print(intersection)

    for i in tmp_cities:
        tmp_text_values = i["Локация"] + " " + i["Тематика"] + " " + i["Направление"] + " " + i["Область"] + " "
        if i["Вид природы"] is not None:
            tmp_text_values += i["Вид природы"] + " "
        if i["Историческая эпоха"] is not None:
            tmp_text_values += i["Историческая эпоха"] + " "
        if i["Историческая личность"] is not None:
            tmp_text_values += i["Историческая личность"] + " "
        if len(set(parser(tmp_text_values)) &
               intersection) == len(intersection):
            res_cities.append(i)

    if len(res_cities) != 0:
        print("if len(res_cities) != 0:")
        return res_cities, 1
    return tmp_cities, 0


def price_city(phrase, tmp_cities):
    res_cities = []

    selected_attributes = "Цена"
    count = 0
    num_cities = cities.shape[0]

    phrase_word = phrase[0]
    for i in (tmp_cities):
        if ('дёшевый' in set(phrase) or 'дёшево' in set(phrase)):
            if i[selected_attributes] < 6000:
                res_cities.append(i)
        elif ('нормальный' in set(phrase) or 'нормально' in set(phrase)):
            if i[selected_attributes] >= 6400 and i[selected_attributes] < 6800:
                res_cities.append(i)
        elif ('доступный' in set(phrase) or 'доступно' in set(phrase)):
            if i[selected_attributes] >= 6800 and i[selected_attributes] <= 7200:
                res_cities.append(i)
        elif ('комфортный' in set(phrase) or 'комфортно' in set(phrase)):
            if i[selected_attributes] >= 7200 and i[selected_attributes] < 7800:
                res_cities.append(i)
        elif ('дорого' in set(phrase) or 'дорогой' in set(phrase)):
            if i[selected_attributes] >= 7800:
                res_cities.append(i)

    if len(res_cities) != 0:
        print("if len(res_cities) != 0:")
        return res_cities, 1
    return tmp_cities, 0


def distance_city(phrase, tmp_cities):
    res_cities = []

    if ('не' in set(phrase) and 'очень' in set(phrase) and
            ('близко' in set(phrase) or 'близкий' in set(phrase))):

        for i in (tmp_cities):
            if (i['Расстояние от Москвы'] >= 100 and
                    i['Расстояние от Москвы'] <= 300):
                res_cities.append(i)



    elif ('не' in set(phrase) and 'очень' in set(phrase) and
          ('далеко' in set(phrase) or 'далёкий' in set(phrase))):
        count = 0
        num_cities = cities.shape[0]

        for i in (tmp_cities):
            if (i['Расстояние от Москвы'] <= 100):
                res_cities.append(i)



    elif (len(set(phrase) & {'близко', 'близкий'}) != 0):
        count = 0
        num_cities = cities.shape[0]

        for i in (tmp_cities):
            if (i['Расстояние от Москвы'] <= 200):
                res_cities.append(i)

        if count == 0:
            print('\nТакого не существует...')

    elif (len(set(phrase) & {'средне', 'средней'}) != 0):
        count = 0
        num_cities = cities.shape[0]

        for i in (tmp_cities):
            if (i['Расстояние от Москвы'] >= 300 and
                    i['Расстояние от Москвы'] <= 500):
                res_cities.append(i)



    elif (len(set(phrase) & {'далеко', 'далёкий'}) != 0):
        count = 0
        num_cities = cities.shape[0]

        for i in (tmp_cities):
            if (i['Расстояние от Москвы'] >= 400):
                res_cities.append(i)

    if len(res_cities) != 0:
        print("if len(res_cities) != 0:")
        return res_cities, 1
    return res_cities, 0
