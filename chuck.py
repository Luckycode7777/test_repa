import requests  # импортировали библу Реквест, что бы отправлять запросы

url = "https://api.chucknorris.io/jokes/random"  # в перем поместили ссыль к которой будем обращаться
print(url)  # вывели ее на печать
result = requests.get(url)  # поместили в перем result поместили запрос requests.get(url)
print(f'статус код: " + {result.status_code}')  # вывели ее на печать статус код
assert 200 == result.status_code  # осуществили проверку
if result.status_code == 200:  # записали условие,что если ...
    print("Успех")
else:
    "Почти"
result.encoding = 'utf-8'
print(result.text)
