from django.db import models
from django.contrib.auth.models import User

class Professores(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    disponibilidade = models.CharField(max_length=19)

class Disciplina(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)

class Turma(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    turno = models.CharField(max_length=5)
