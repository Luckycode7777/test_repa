import requests


class Test_only_one_category():
    """Создание только одной категории"""



    def test_get_only_one_category(self):
        """Получение только одной категории"""

        url = "https://api.chucknorris.io/jokes/categories"
        print(f'Ссылка для получения всех категорий: {url}')
        result = requests.get(url)
        print(result.status_code)  # получение статус кода
        assert 200 == result.status_code
        if result.status_code == 200:
            print("SUCCESS")
        else:
            print("ERROR")
        result.encoding = 'utf-8'
        print(result.text)
        print("=====" * 30)
        print("======= ВСЕ КАТЕГОРИИ =======")

        # Выводим все категории для юзера
        view = result.json()
        for i in view:
            print(i)
        print("=====" * 8)

        select = input("Выберите категорию и введите ее название: ")
        print("Вы ввели: " + select)

        pro = select
        if pro in view:
            print("Такая категория есть: " + pro)

            # выводим рабочую ссылку по выбранной категории
            your_select = f"https://api.chucknorris.io/jokes/random?category={select}"
            print(f"Это ваша ссылка: {your_select}")
            res = requests.get(your_select)
            check = res.json()
            check_info = check.get("value")
            print(f"Эта шутка от Чака, по выбранной категории: {check_info}")

            # проверка на слово в шутке
            name = "Chuck"
            if name in check_info:
                print("Chuck привет")
            else:
                print("Chuck тебя здесь нет")

        else:
            print("Такой категории нет: " + pro)


one = Test_only_one_category()
one.test_get_only_one_category()
