import requests
import json  # импортируем необходимую библиотеку

r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
texts = json.loads(r.content)  # делаем из полученных байтов python объект для удобной работы
print(type(texts))  # проверяем тип сконвертированных данных

for text in texts:  # выводим полученный текст. Но для того чтобы он влез в консоль оставим только первые 50 символов.
    print(text[:50], '\n')