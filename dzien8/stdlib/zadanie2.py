from urllib.request import urlopen
import json

# with urlopen("http://api.nbp.pl/api/cenyzlota?format=json") as plik:
#     napis = plik.read().decode('utf-8')
#
# print(type(napis))
# print(napis)
# obiekt = json.loads(napis)
# cena = obiekt[0]['cena']
# print(f"Obecna cena złota wynosi {cena} PLN")

gdzie = input("Podaj miasto: ")

with urlopen(f"https://www.metaweather.com/api/location/search/?query={gdzie}") as plik:
    wynik = json.loads(plik.read().decode('utf-8'))

woeid = wynik[0]['woeid']
print(f"WOEID: {woeid}")

with urlopen(f"https://www.metaweather.com/api/location/{woeid}/") as plik:
    wynik = json.loads(plik.read().decode('utf-8'))

prognozy = wynik['consolidated_weather']
for prognoza in prognozy:
    print(f"Prognoza na dzień {prognoza['applicable_date']}:")
    print(f"\tTemp: {prognoza['min_temp']:.2f} - {prognoza['max_temp']:.2f}")
