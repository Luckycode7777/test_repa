import requests  # импортировали библу Реквест, что бы отправлять запросы


class Test_new_joke():
    """Создание новой шутки"""

    def __init__(self):
        pass  # метод init, которы ни чего не будет в себя включать

    # def test_create_new_joke(self):
    #     """Создание случайно шутки"""
    #
    #     url = "https://api.chucknorris.io/jokes/random"  # в перем-ю поместили ссыль к которой будем обращаться
    #     print(url)  # вывели ее на печать
    #     result = requests.get(url)  # поместили в перем result поместили запрос requests.get(url)
    #     print(f'статус код: " + {result.status_code}')  # вывели ее на печать статус код
    #     assert 200 == result.status_code  # осуществили проверку
    #     if result.status_code == 200:  # записали условие,что если ...
    #         print("Успех")
    #     else:
    #         "Почти"
    #     result.encoding = 'utf-8'
    #     print(result.text)
    #
    #     check = result.json()
    #     check_info = check.get("categories")
    #     assert check_info == []
    #     print("Категория верна")
    #     print(f'categories: {check_info}')
    #     check_info_1 = check.get("id")
    #     print(f'id: {check_info_1}')
    #
    #     check_info_3 = check.get("value")
    #     print(check_info_3)
    #     name = "Chuck"
    #     if name in check_info_3:
    #         print("Chuck привет")
    #     else:
    #         print("Chuck тебя здесь нет")

    def test_create_new_random_category_joke(self):
        """Создание случайно категории шутки"""

        category = "sport"
        # в перем-ю поместили ссыль к которой будем обращаться и произвели конкотинацию
        url = "https://api.chucknorris.io/jokes/random?category=" + category
        print(url)  # вывели ее на печать
        result = requests.get(url)  # поместили в перем result поместили запрос requests.get(url)
        print(f'статус код: {result.status_code}')  # вывели ее на печать статус код
        assert 200 == result.status_code  # осуществили проверку
        if result.status_code == 200:  # записали условие,что если ...
            print("Успех")
        else:
            "Почти"
        result.encoding = 'utf-8'
        print(result.text)

        check = result.json()
        check_info = check.get("categories")
        assert check_info == ["sport"]
        print("Категория верна")
        print(f'categories: {check_info}')
        # check_info_1 = check.get("id")
        # print(f'id: {check_info_1}')
        #
        check_info_3 = check.get("value")
        print(check_info_3)
        name = "Chuck"
        if name in check_info_3:
            print("Chuck привет")
        else:
            print("Chuck тебя здесь нет")

# random_joke = Test_new_joke()  # создали перем random_joke и указали экземпляром какого класса она является
# random_joke.test_create_new_joke()  # вызвали метод test_create_new_joke()

sport_joke = Test_new_joke()
sport_joke.test_create_new_random_category_joke()