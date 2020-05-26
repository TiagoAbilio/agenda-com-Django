from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Eventos(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_event = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True) #auto_now aplica de forma auto o horario de criacao
    # mudando nome da tabela
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    #o on_delete=models.CASCADE() dis que quando excluido o usuario ira exclir tudo que ele esta associado
    class Meta:
        db_table = 'Eventos'

    def __str__(self):
        return self.titulo;
