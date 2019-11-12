from django.db import models

# Create your models here.
class Video(models.Model):
    nome = models.CharField(max_length=50)
    duracao = models.IntegerField()
    data_publicacao = models.DateTimeField()
    endereco = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Tag(models.Model):
    nome = models.CharField(max_length=50)