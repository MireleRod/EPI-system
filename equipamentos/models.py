from django.db import models


class Equipamento(models.Model):
    STATUS_EMPRESTADO = 'emprestado'
    STATUS_FORNECIDO = 'fornecido'
    STATUS_DEVOLVIDO = 'devolvido'
    STATUS_DANIFICADO = 'danificado'
    STATUS_PERDIDO = 'perdido'

    STATUS_CHOICES = [
        (STATUS_EMPRESTADO, 'Emprestado'),
        (STATUS_FORNECIDO, 'Fornecido'),
        (STATUS_DEVOLVIDO, 'Devolvido'),
        (STATUS_DANIFICADO, 'Danificado'),
        (STATUS_PERDIDO, 'Perdido'),
    ]

    nome = models.CharField(max_length=150)
    codigo = models.CharField(max_length=50, unique=True)
    tipo = models.CharField(max_length=100)
    classe_risco = models.CharField(max_length=100)
    data_aquisicao = models.DateField(blank=True, null=True)
    data_devo = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_FORNECIDO)

    def __str__(self):
        return f"{self.nome} ({self.codigo})"
