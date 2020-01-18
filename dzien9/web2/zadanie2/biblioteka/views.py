from django.shortcuts import render, get_object_or_404
from biblioteka.models import Autor, Ksiazka

# Create your views here.
def lista_autorow(request):
    lista = Autor.objects.all()
    return render(request, template_name="lista_autorow.html",
                  context={"lista": lista})

def szczegoly_autora(request, id):
    a = get_object_or_404(Autor, id=id)
    lista = Ksiazka.objects.filter(autor__id=id)
    return render(request, "autor.html",
                  context={"autor": a, "lista_ksiazek": lista})
