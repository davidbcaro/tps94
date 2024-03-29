from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripción')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        db_table = 'categoria'
        ordering = ['id']


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    price = models.FloatField(verbose_name='Precio')
    description = models.TextField(verbose_name='Descripción')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'producto'
        ordering = ['id']


