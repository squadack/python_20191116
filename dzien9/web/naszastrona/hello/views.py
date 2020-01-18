from django.shortcuts import render, Http404, get_object_or_404
from django.http import HttpResponse

from hello.models import Product

# Create your views here.
def hello(request, imie):
    return HttpResponse(f"Witaj {imie}")

def dzialanie(request, op, a, b):
    if op == "add":
        return HttpResponse(f"{a} + {b} = {a + b}")
    elif op == "sub":
        return HttpResponse(f"{a} - {b} = {a - b}")
    elif op == "mul":
        return HttpResponse(f"{a} * {b} = {a * b}")
    elif op == "div":
        return HttpResponse(f"{a} / {b} = {a / b}")
    else:
        raise Http404("Zła operacja!")

def lista_produktow(request):
    lista = Product.objects.filter(dostepny=True)
    return render(request, template_name="lista_produktow.html",
                  context={"zmienna": 15, "produkty": lista})


def produkt(request, id):
    # p = Product.objects.get(id=id)
    p = get_object_or_404(Product, id=id)
    return render(request, template_name="szczegoly_produktu.html",
                  context={"produkt": p})