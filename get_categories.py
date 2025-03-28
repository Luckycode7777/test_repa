import requests


class Test_more_joke():
    """"Создание множества шуток"""

    def __init__(self):
        pass

    def test_get_categories(self):
        """"Получение всех категорий шуток"""
        url = "https://api.chucknorris.io/jokes/categories"
        print(f'Ссылка для получения всех категорий: {url}')
        result = requests.get(url)
        print(f'Статус код: {result.status_code}')
        assert 200 == result.status_code
        if result.status_code == 200:
            print("Успех")
        else:
            print("Ошибка")
        result.encoding = 'utf-8'
        print(result.text)
        print("=====" * 20)

        view = result.json()
        for category in view:
            url = f"https://api.chucknorris.io/jokes/random?category={category}"
            res = requests.get(url)
            print(res.text)
            check = res.json()
            check_info = check.get("value")
            print(check_info)
            name = "Chuck"
            if name in check_info:
                print("Chuck привет")
            else:
                print("Chuck тебя здесь нет")
            print("=====" * 10)


categor = Test_more_joke()
categor.test_get_categories()
