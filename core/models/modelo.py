from djando.db import models


class Modelo(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.CharField(max_length=100, required=False)
    categorria = models.CharField(max_length=100, required=False)

    def __str__(self):
        return self.nome
