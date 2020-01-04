def vowels(napis):
    for znak in napis:
        if znak.lower() in "aeiouy":
            yield znak


for x in vowels("Ala ma kota"):
    print(f" - {x}")