from django.db import models
from apps.base.models import BaseModel

# Create your models here.


class MeasureUnit(BaseModel):
    description = models.CharField(
        'description', max_length=50, blank=False, null=False, unique=True)

    class Meta:
        verbose_name = 'Unidad de medida'
        verbose_name_plural = 'Unidades de medidas'

    def __str__(self):
        return self.description


class Category(BaseModel):
    description = models.CharField(
        'description', max_length=50, blank=False, null=False, unique=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.description


class Product(BaseModel):
    name = models.CharField('name', max_length=150,
                            blank=False, null=False, unique=True)
    description = models.TextField('description', blank=False, null=False)
    measure_unit = models.ForeignKey(
        MeasureUnit, on_delete=models.CASCADE, verbose_name='measure unit', null=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name='category', null=True)

    class Meta:
        verbose_name = 'Productos'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.name
