from tabnanny import verbose
from django.db import models

# Create your models here.
class Mouses(models.Model):
    id = models.AutoField(primary_key=True)
    producto = models.TextField(max_length=10, verbose_name='Productoo')
    img = models.TextField(max_length=10, verbose_name='link de la image', null=True)
    precio = models.IntegerField(verbose_name='Precio', null=True)
