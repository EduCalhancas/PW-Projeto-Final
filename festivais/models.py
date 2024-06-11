from django.db import models

# Create your models here.


class Localizacao(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Banda(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Festival(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE)
    bandas = models.ManyToManyField(Banda, related_name='bandas')
    cartaz = models.ImageField(upload_to="cartaz", null=True, blank=True, default=None)

    def __str__(self):
        return self.nome