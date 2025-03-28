import requests


class Test_new_more_locations():
    """Работа с новыми локациями"""

    def __init__(self):
        pass

    def test_create_new_locations(self):
        """Создание новых локаций"""

        print("======" * 9)
        print(">>>> Запуск теста <<<<")
        print("======" * 9, '\n')

        print("Вывод новых place_id")
        print("======" * 5)
        for i in range(5):
            base_url = "https://rahulshettyacademy.com"  # базовый url
            key = "?key=qaclick123"  # переменная передаваемых параметров для всех запросов

            post_resource = "/maps/api/place/add/json"  # ресурс метода POST

            # сохраняем тело запроса body в переменную json_for_create_new_location
            json_for_create_new_location = {
                "location": {
                    "lat": -38.383494,
                    "lng": 33.427362
                }, "accuracy": 50,
                "name": "Frontline house",
                "phone_number": "(+91) 983 893 3937",
                "address": "29, side layout, cohen 09",
                "types": [
                    "shoe park",
                    "shop"
                ],
                "website": "http://google.com",
                "language": "French-IN"
            }

            # создаем url запрос которы будет включать в себя все три параметра, что выше ^^^^
            post_url = base_url + post_resource + key

            # отправляем запрос по методу post
            result_post = requests.post(post_url, json=json_for_create_new_location)

            # в перем-ю check_post сохраняем json-овский запрос нашего ответа
            check_post = result_post.json()
            place_id = check_post.get("place_id")  # хотим получить значение поля "place_id"
            print(f"Значение поля place_id: {place_id}")

            pl_id = open('doc/file.txt', 'a')  # открываем папку и читаем place_id из файла
            pl_id.write(f'{place_id}\n')
            pl_id.close()
            continue

    def test_read_locations_from_file(self):
        """Чтение локаций из файла и поочередный вывод"""

        print("======" * 5, '\n')
        print("Вывод списка локаций")
        print("======" * 5)

        with open('doc/file.txt') as f:
            mylist = f.read().splitlines()  # читаем список без переноса \n в конце каждого значение
            print(mylist)
        print("======" * 5, '\n')
        print("Вывод каждой локации и проверка")
        print("======" * 5)

        for x in mylist:
            base_url = "https://rahulshettyacademy.com"  # базовая url
            key = "?key=qaclick123"  # переменная передаваемых параметров для всех запросов

            get_resource = "/maps/api/place/get/json"  # ресурс метода GET

            get_url = base_url + get_resource + key + "&place_id=" + x
            print(get_url)
            result_get = requests.get(get_url)
            print(result_get.text)  # выводим body на печать
            assert 200 == result_get.status_code
            print("SUCCESS")
            print("======" * 9, '\n')

    def test_delete_two_locations(self):
        """Удаление двух локаций"""

        with open('doc/file.txt') as f:
            mylist = f.read().splitlines()  # читаем список без переноса \n в конце каждого значение
            print(mylist)

        for k in mylist[1:: 2]:
            base_url = "https://rahulshettyacademy.com"  # базовая url
            key = "?key=qaclick123"  # переменная передаваемых параметров для всех запросов
            delete_resource = "/maps/api/place/delete/json"
            delete_url = base_url + delete_resource + key
            print(delete_url)

            json_for_delete_location = {
                "place_id": k
            }

            result_delete = requests.delete(delete_url, json=json_for_delete_location)
            print(result_delete.text)
            assert 200 == result_delete.status_code
            print("SUCCESS")

    def test_create_three_works_locations(self):
        """Отбор существующих локаций и помещение их в новый файл"""

        with open('doc/file.txt') as f:
            mylist = f.read().splitlines()  # читаем список без переноса \n в конце каждого значение
            print(mylist)

        for x in mylist:
            base_url = "https://rahulshettyacademy.com"  # базовая url
            key = "?key=qaclick123"  # переменная передаваемых параметров для всех запросов

            get_resource = "/maps/api/place/get/json"  # ресурс метода GET

            get_url = base_url + get_resource + key + "&place_id=" + x
            print(get_url)
            result_get = requests.get(get_url)
            print(result_get.text)  # выводим body на печать
            if result_get.status_code == 200:
                # создание новой папки для рабочих place_id
                pl_id = open('doc/file_works_place_id.txt', 'a')  # открываем папку и читаем place_id из файла
                pl_id.write(f'{x}\n')
                pl_id.close()
                print("SUCCESS")
            elif result_get.status_code == 404:
                print("ERROR")
            else:
                print("UNKNOWN")
            print("======" * 9, '\n')

        print(">>>>>>Тестирование Test_new_location завершено успешно!<<<<<<")


new_place = Test_new_more_locations()
new_place.test_create_new_locations()  # выводим на печать post_url

new_place_get = Test_new_more_locations()
new_place_get.test_read_locations_from_file()

delete_place_id = Test_new_more_locations()
delete_place_id.test_delete_two_locations()

three_place_id = Test_new_more_locations()
three_place_id.test_create_three_works_locations()
