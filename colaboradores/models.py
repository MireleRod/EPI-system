from django.db import models

class Colaborador(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=20)
    cargo = models.CharField(max_length=100)
    setor = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)
