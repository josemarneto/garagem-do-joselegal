from django.db import models


class Veiculo(models.Model):
    ano = models.IntegerField(null=True, blank=True, default=0)
    preco = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, default=0)
    modelo = models.ForeignKey('Modelo', on_delete=models.CASCADE, null=True, blank=True)
    cor = models.ForeignKey('Cor', on_delete=models.CASCADE, null=True, blank=True)
    acessorios = models.ManyToManyField('Acessorio', blank=True)

    def __str__(self):
        return f'{self.modelo.upper()} - {self.ano} - {self.cor}'
