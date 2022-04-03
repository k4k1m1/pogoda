import requests

m = input("Podaj nazwę miasta, którego dane pogodowe chcesz sprawdzić: ")

www = requests.get(f'https://wttr.in/{m}?format=j1')

dane = www.json()
lokalizacja = dane['nearest_area'][0]['areaName'][0]['value']
temp = dane['current_condition'][0]['temp_C']
feels = dane['current_condition'][0]['FeelsLikeC']
wind = dane['current_condition'][0]['windspeedKmph']
zachm = dane['current_condition'][0]['cloudcover']

print(f'Twoja najbliższe osiedle dla {m}: {lokalizacja}')
print(f'Temperatura w {m}: {temp}°C')
print(f'Odczuwalna w {m}: {feels}°C')
print(f'Wiatr w {m}: {wind} km/h')
print(f'Zachmurzenie w {m}: {zachm}%')


    # print(f"Name: {h[0]['name']}")
    # print(f"Status: {h[0]['status']}")
    # print(f"Species: {h[0]['species']}")
    # print(f"Image: {h[0]['image']}")
    # postac = requests.get(h[0]['url'])
    # dane_postaci = postac.json()
    # for element in dane_postaci:
    #     print(element)

    # return {
    #     "name": h[0]['name'],
    #     "status": h[0]['status'],
    #     "species": h[0]['species'],
    #     "image": h[0]['image'],
    # }