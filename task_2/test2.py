import json
import pandas as pd
import requests


# Получение данных с API
def weather_results():
    url = f"http://api.openweathermap.org/data/2.5/weather?q=москва&lang=ru&appid=d67210d769cb6fa4c327b6270353ebee&units=metric"
    r = requests.get(url)
    response_json = json.loads(r.content)
    data = []
    data.append(response_json['name'])
    data.append(response_json['main']['temp'])
    data.append(response_json['main']['feels_like'])
    data.append(response_json['main']['temp_min'])
    data.append(response_json['main']['temp_max'])
    data.append(response_json['main']['humidity'])
    data.append(response_json['wind']['speed'])

    headings = ["Город", "Температура", "Ощущается", "Мин. температура", "Макс. температура", "Влажность", "Скорость ветра"]
    result = pd.DataFrame([data], columns=headings)

    print(result)


weather_results()
