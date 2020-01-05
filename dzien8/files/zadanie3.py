with open("emails.txt") as plik:
    wiersze = plik.readlines()

# zbior = {wiersz.strip().lower() for wiersz in wiersze if wiersz.count("@") == 1}
zbior = set()

for wiersz in wiersze:
    # napis = wiersz.lstrip().rstrip()
    napis = wiersz.strip()
    napis = napis.lower()
    if napis.count("@") == 1:
        zbior.add(napis)

with open("clean_emails.txt", mode="w") as plik:
    for email in sorted(zbior):
        plik.write(email)
        plik.write("\n")
