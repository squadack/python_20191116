from django.db import models

# Create your models here.
class Osoba(models.Model):
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)
    nr_dowodu = models.CharField(max_length=9)

    def __str__(self):
        return f"({self.id}) {self.imie} {self.nazwisko}"

class Product(models.Model):
    nazwa = models.CharField(max_length=30)
    opis = models.TextField()
    cena = models.DecimalField(max_digits=6, decimal_places=2)
    dostepny = models.BooleanField()
