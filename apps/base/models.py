from django.db import models

# Create your models here.


class BaseModel(models.Model):
    """Model definition for MODELNAME."""

    # TODO: Define fields here
    id = models.AutoField(primary_key=True)
    state = models.BooleanField('State', default=True)
    created_date = models.DateField(
        'Creation date', auto_now=False, auto_now_add=True)
    updated_date = models.DateField(
        'Update date', auto_now=True, auto_now_add=False)
    deleted_date = models.DateField(
        'Deletion date', auto_now=True, auto_now_add=False)

    class Meta:
        """Meta definition for MODELNAME."""
        abstract = True
        verbose_name = 'Modelo base'
        verbose_name_plural = 'Modelos base'
