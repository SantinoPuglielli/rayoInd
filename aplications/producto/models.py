from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    #precio = models.DecimalField('Precio', max_digits=6, decimal_places=2)
    precio= models.IntegerField('Precio')
    descripcion = models.TextField('Descripción', null=True)
    imagen = models.ImageField('Imagen')
    filtros = models.TextField('Filtros', null=True)

    def __str__(self):
        return self.nombre