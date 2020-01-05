from os import scandir

def wypisz_katalog(kat, poziom=0):
    for x in scandir(kat):
        print(poziom * "\t", x.name, x.is_dir())
        if x.is_dir():
            wypisz_katalog(x, poziom + 1)

# wypisz_katalog(r"C:\Users\kurs\Desktop", 0)
wypisz_katalog(r"../..")