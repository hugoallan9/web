from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Tipo_Cambio(models.Model):
    fecha = models.DateTimeField('fecha de cambio')
    cambio = models.FloatField()
