from django.db import models
from apps.base.models import BaseModel

# Create your models here.


class MeasureUnit(BaseModel):
    """Model definition for MODELNAME."""

    # TODO: Define fields here
    description = models.CharField(
        'description', max_length=50, blank=False, null=False, unique=True)

    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'Unidad de medida'
        verbose_name_plural = 'Unidades de medidas'

    def __str__(self):
        return self.description


class Category(BaseModel):
    """Model definition for MODELNAME."""

    # TODO: Define fields here
    description = models.CharField(
        'description', max_length=50, blank=False, null=False, unique=True)
    measure_unit = models.ForeignKey(
        MeasureUnit, on_delete=models.CASCADE, verbose_name='measure unit')

    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.description


class Product(BaseModel):
    """Model definition for MODELNAME."""

    # TODO: Define fields here
    name = models.CharField('name', max_length=150,
                            blank=False, null=False, unique=True)
    description = models.TextField('description', blank=False, null=False)

    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'Productos'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.name
