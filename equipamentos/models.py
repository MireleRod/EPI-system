from django.db import models


class Equipamento(models.Model):
    nome = models.CharField(max_length=150)
    codigo = models.CharField(max_length=50, unique=True)
    tipo = models.CharField(max_length=100)
    classe_risco = models.CharField(max_length=100)
    data_aquisicao = models.DateField(blank=True, null=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome} ({self.codigo})"
