from django.http import HttpResponse
from django.shortcuts import render
from .models import Categoria


def index(request):
    return HttpResponse("Hello World")

def contact(request, name):
    return HttpResponse(f"Hello {name}")

def categorias(request):
    filtro = request.GET.get('nombre', None) # Parametro enviado

    # Filtrar categorias
    if filtro: # Filtra por la condición del parametro enviado
        categorias = Categoria.objects.filter(nombre=filtro) # Si puede usar icontains para que haga la distinción entre mayúsculas y minúsculas 
    else: # Si no enviaron el parametro, muestra todo
        categorias = Categoria.objects.all() 

    return render(request, "categorias.html", {
        "categorias": categorias
    })