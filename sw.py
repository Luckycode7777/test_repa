import json
import requests


class Test_star_wars_names():
    """Получение всех героев игравших с ДВ"""

    def __init__(self):
        pass

    def get_all_data_with_dr(self):
        """Получение всех данных с Дарт Вейдером"""
        base_url = "https://swapi.dev/api/"
        people = "people/"
        number = "4/"

        get_url = base_url + people + number
        print(f'Адрес Darth Vader >>>  {get_url}')
        print("=====" * 8, "\n")

        result_get = requests.get(get_url)
        print(result_get.text)
        assert 200 == result_get.status_code
        print("SUCCESS")
        print("=====" * 8, "\n")
        # проверка имени
        check = result_get.json()
        check_info = check.get("name")
        name = "Darth Vader"
        if name in check_info:
            print("Это Darth Vader!")
        else:
            print("Ошибка! это другой персонаж.")

        print("=====" * 8, "\n")
        print("получить все ключи >>>>")
        # получить все ключи
        token = json.loads(result_get.text)
        print(list(token))  # распечатываем все поля что есть

        """Вывод на печать всех фильмов, всех персонажей, уникальных имен"""
        result_films = result_get.json()
        result_films_1 = result_films.get("films")
        print("=====" * 8, "\n")
        print("все адреса фильмов")
        print(result_films_1)
        # цикл для получения всех персонажей
        for z in result_films_1[:]:
            print(z)
            take = requests.get(z)
            res_characters = take.json()
            assert 200 == result_get.status_code
            print("SUCCESS")
            print("=====" * 8, "\n")
            res_characters_1 = res_characters.get("characters")
            print(f'адреса персонажей \n {res_characters_1}')
            print("=====" * 8, "\n")
            print("Имена персонажей: ")
            # цикл для получения имен
            for j in res_characters_1[:]:
                names = requests.get(j)
                take_name = names.json()
                take_real_name = take_name.get("name")
                print(take_real_name)

                # Запись имен в первый файл с дублями
                pl_id = open('doc/file_all_name.txt', 'a', encoding='utf-8')
                pl_id.write(f'{take_real_name}\n')
                pl_id.close()

                # Запись уникальных имен
                lines = open('doc/file_all_name.txt').read().split('\n')
                unique_lines = list(set([x for x in lines]))
                open('doc/file_unique_names.txt', 'w').write('\n'.join(unique_lines))
            print("=====" * 8, "\n")
        print(">>>>>>Тестирование Test_new_location завершено успешно!<<<<<<")


get_all_date = Test_star_wars_names()
get_all_date.get_all_data_with_dr()
