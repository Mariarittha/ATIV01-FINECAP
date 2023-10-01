from django.db import models
from django.utils.translation import gettext_lazy as _


class Stand(models.Model):
    localizacao = models.CharField(max_length=150)
    valor = models.FloatField()
    
    def __str__(self):
        return f"{self.pk} | {self.localizacao} | {self.valor}"