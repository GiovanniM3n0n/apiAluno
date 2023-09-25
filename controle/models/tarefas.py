from django.db import models
from controle.models.aluno import Aluno
from controle.models.disciplina import Disciplina

class Tarefas(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    data_entrega = models.DateField(null=False)
    concluida = models.BooleanField(default=False)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    disciplinas = models.ManyToManyField(Disciplina)