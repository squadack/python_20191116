import re

wyrazenie = re.compile(r"ab*c")
kody_pocztowe = re.compile(r"\b\d{2}-\d{3}\b")
daty = re.compile(r"\b\d{2} [A-Z][a-z]{2} \d{4}\b")


with open("regex.txt") as plik:
    napis = plik.read()

wynik = wyrazenie.findall(napis)
print(wynik)