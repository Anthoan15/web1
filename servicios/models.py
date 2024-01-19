from django.db import models

# Create your models here.

class Producto(models.Model):
    titulo=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=50)
    precio=models.DecimalField(max_digits=30, decimal_places=2)
    imagen=models.ImageField(upload_to='servicios')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'

    def __str__(self):
        return self.titulo  