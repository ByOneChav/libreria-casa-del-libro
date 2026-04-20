from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    # get
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Editora(models.Model):
    nombreEditora = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombreEditora

class Libro(models.Model):
    nombreLibro = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, null=False)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE, null=False)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    fechaPublicacion = models.DateField()
    imagen = models.ImageField(upload_to='media/', null=True, blank=True)
    siposis = models.TextField(null=False)
    disponibilidad = models.BooleanField(default=True)

    def __str__(self):
        return self.nombreLibro
    
