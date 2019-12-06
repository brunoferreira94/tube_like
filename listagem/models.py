from django.db import models

class Video(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    nome = models.CharField(max_length=50)
    duracao = models.CharField(max_length=10)
    data_publicacao = models.DateTimeField()
    endereco = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Tag(models.Model):
    nome = models.CharField(max_length=50)
    video = models.ManyToManyField(Video, through='Video_tag')
    def __str__(self):
        return self.nome

class Video_tag(models.Model):
    video_id = models.ForeignKey(Video, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome

class Pornstar(models.Model):
    nome = models.CharField(max_length=50)
    video = models.ManyToManyField(Video, through='Video_pornstar')
    def __str__(self):
        return self.nome

class Video_pornstar(models.Model):
    video_id = models.ForeignKey(Video, on_delete=models.CASCADE)
    pornstar_id = models.ForeignKey(Pornstar, on_delete=models.CASCADE)
