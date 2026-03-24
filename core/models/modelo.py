from django.db import models


class Modelo(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.CharField(max_length=100, null=True, blank=True)
    categorria = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'({self.id}) - {self.nome}'
