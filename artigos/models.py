from django.db import models

# Create your models here.

class Artigo(models.Model):
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    autor = models.CharField(max_length=255)
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.titulo
