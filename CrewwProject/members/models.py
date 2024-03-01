from django.db import models

class Member(models.Model):
  PrimerNombre = models.CharField(max_length=255)
  UltimoNombre = models.CharField(max_length=255)
  Telefono = models.IntegerField(null=True)
  Fecha_Ingreso = models.DateField(null=True)