from django.db import models

# Create your models here.

class Banda(models.Model):
    nome = models.CharField(max_length=100)
    membros = models.TextField()
    descricao = models.TextField()
    foto = models.ImageField(upload_to='bandas/')

    def _str_(self):
        return self.nome

class Album(models.Model):
    titulo = models.CharField(max_length=100)
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE)
    data_lancamento = models.PositiveIntegerField()
    capa = models.ImageField(upload_to='capas/')

    def _str_(self):
        return self.titulo

class Musica(models.Model):
    titulo = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    link_do_spotify = models.URLField(blank=True, null=True)

    def _str_(self):
        return self.titulo