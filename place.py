import requests


class Test_new_location():
    """Работа с новой локацией"""

    def test_create_new_location(self):
        """Создание новой локации"""

        base_url = "https://rahulshettyacademy.com"  # базовая url
        key = "?key=qaclick123"  # переменная передаваемых параметров для всех запросов

        """Создание новой локации"""

        post_resource = "/maps/api/place/add/json"  # ресурс метода POST

        # создаем url запрос которы будет включать в себя все три параметра, что выше ^^^^
        post_url = base_url + post_resource + key
        print(post_url)

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

        # отправляем запрос по методу post
        result_post = requests.post(post_url, json=json_for_create_new_location)

        print(result_post.status_code)
        assert 200 == result_post.status_code  # проверяем ст код наш ответа. Мы ожидаем статус код 200
        if result_post.status_code == 200:  # нам пришел статус код 200
            print("Успех, создана новая локация")
        else:
            print("Ошибка")

        check_post = result_post.json()  # в перем-ю check_post сохраняем json-овский запрос нашего ответа
        # в пер check_info_post, сохраняем значение поля "status". get что-бы получить поле статус и ...
        check_info_post = check_post.get("status")
        print(f"Статус кода ответа: {check_info_post}")  # ... и водим на печать
        assert check_info_post == "OK"  # делаем проверку, что "status":"OK"
        print("Статус кода ответа верен")
        place_id = check_post.get("place_id")  # хотим получить значение поля "place_id"
        print(f"Значение поля place_id: {place_id}")

        """Проверка создания новой локации"""

        get_resource = "/maps/api/place/get/json"  # ресурс метода GET
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)
        assert 200 == result_get.status_code
        if result_get.status_code == 200:
            print("Успех! Проверка, создания новой локации прошла успешно")
        else:
            print("Ошибка")

        """Изменение новой локации"""

        put_resource = "/maps/api/place/update/json"  # ресурс метода put
        put_url = base_url + put_resource + key
        print(put_url)

        json_for_update_new_location = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }

        result_put = requests.put(put_url, json=json_for_update_new_location)
        print(result_put.text)

        print(result_put.status_code)
        assert 200 == result_put.status_code
        if result_put.status_code == 200:
            print("Успех! Проверка, изменения новой локации")
        else:
            print("Ошибка")

        check_put = result_put.json()
        check_put_info = check_put.get("msg")
        print(f"Значение поля msg: {check_put_info}")
        assert check_put_info == "Address successfully updated"
        print("Сообщение верно!")

        """Проверка изменения новой локации"""

        result_get = requests.get(get_url)
        print(result_get.text)
        assert 200 == result_get.status_code
        if result_get.status_code == 200:
            print("Успех! Проверка, изменения новой локации прошла успешно")
        else:
            print("Ошибка")

        check_adress = result_get.json()  # в пер check_adress сохранили json ответ result_get.json()
        check_adress_info = check_adress.get("address")  # в перем check_adress_info, сохраняем значение поля "address"
        print(check_adress_info + "<<<<<<<<")
        assert check_adress_info == "100 Lenina street, RU"  # оператор assert
        print("Сообщение верно!" + "<<<<<<<<")

        """Удаление новой локации"""

        delete_resource = "/maps/api/place/delete/json"
        delete_url = base_url + delete_resource + key
        print(delete_url)

        json_for_delete_location = {
            "place_id": place_id
        }

        result_delete = requests.delete(delete_url, json=json_for_delete_location)
        print(result_delete.text)

        print(result_delete.status_code)
        assert 200 == result_delete.status_code
        if result_delete.status_code == 200:
            print("Успех!Проверка удаления новой локации")
        else:
            print("Ошибка")

        check_delete = result_delete.json()
        check_delete_info = check_delete.get("status")
        print(f'Статус кода ответа: {check_delete_info}')
        assert check_delete_info == "OK"
        print("Статус кода ответа верен!")

        """Проверка удаления новой локации"""

        result_get = requests.get(get_url)
        print(result_get.text)
        assert 404 == result_get.status_code  # ожидаем здесь ошибку
        if result_get.status_code == 404:
            print("Успех! Проверка, удаления новой локации прошла успешно")
        else:
            print("Ошибка")

        check_msg = result_get.json()  # в пер check_msg сохранили json ответ result_get.json()
        check_msg_info = check_msg.get("msg")  # в перем  check_msg_info, сохраняем значение поля "msg"
        print(check_msg_info + "<<<<<<<<")
        assert check_msg_info == "Get operation failed, looks like place_id  doesn't exists"  # оператор assert
        print("Сообщение верно!" + "<<<<<<<<")

        print(">>>>>>Тестирование Test_new_location завершено успешно!<<<<<<")


new_place = Test_new_location()
new_place.test_create_new_location()  # выводит на печать post_url, что значение корректное у ссылки ^^^^
