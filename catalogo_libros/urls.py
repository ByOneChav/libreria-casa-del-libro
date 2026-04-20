from catalogo_libros import views
from django.urls import path

urlpatterns = [
    path('', views.listaLibros, name='listaLibros'),
]