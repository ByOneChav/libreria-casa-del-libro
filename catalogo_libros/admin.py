from django.contrib import admin
from catalogo_libros.models import Autor, Editora, Libro

# Register your models here.
admin.site.register(Autor)
admin.site.register(Editora)
admin.site.register(Libro)

