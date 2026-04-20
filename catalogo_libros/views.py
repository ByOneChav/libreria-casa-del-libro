from django.shortcuts import render
from catalogo_libros.models import Libro


# Create your views here.
def listaLibros(request):
    libros = Libro.objects.all()
    return render(request, 'catalogo/lista_libros.html', {'libros': libros})
