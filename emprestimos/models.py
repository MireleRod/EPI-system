from django.db import models
from colaboradores.models import Colaborador
from equipamentos.models import Equipamento


class EmprestimoEPI(models.Model):

    class Status(models.TextChoices):
        EMPRESTADO = 'emprestado', 'Emprestado'
        FORNECIDO = 'fornecido', 'Fornecido'
        DEVOLVIDO = 'devolvido', 'Devolvido'
        DANIFICADO = 'danificado', 'Danificado'
        PERDIDO = 'perdido', 'Perdido'

    colaborador = models.ForeignKey(Colaborador, on_delete=models.PROTECT)
    equipamento = models.ForeignKey(Equipamento, on_delete=models.PROTECT)

    data_emprestimo = models.DateTimeField(auto_now_add=True)
    data_prevista_devolucao = models.DateTimeField()
    data_devolucao = models.DateTimeField(null=True, blank=True)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.EMPRESTADO
    )

    observacao_devolucao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.colaborador.nome} - {self.equipamento.nome} ({self.status})"