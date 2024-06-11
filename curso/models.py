from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    apresentacao = models.TextField()
    objetivos = models.TextField()
    competencias = models.TextField()

    def __str__(self):
        return self.nome

class AreaCientifica(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    curricularIUnitReadableCode = models.CharField(max_length=50)
    curricularUnitCode = models.IntegerField()
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    semestre = models.CharField(max_length=100)
    ects = models.IntegerField()
    #falta area cientifica e docentes

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    disciplina = models.OneToOneField(Disciplina, on_delete=models.CASCADE)
    descricao = models.TextField()
    conceitos_aplicados_da_unidade_curricular = models.TextField()
    tecnologias_usadas = models.TextField()
    imagem = models.ImageField(upload_to='projetos_imagens/')
    video_link = models.URLField()
    github_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.disciplina.nome} Projeto"

class LinguagemProgramacao(models.Model):
    nome = models.CharField(max_length=50)
    projetos = models.ManyToManyField(Projeto)

    def __str__(self):
        return self.nome

class Docente(models.Model):
    nome = models.CharField(max_length=100)
    disciplinas = models.ManyToManyField(Disciplina)

    def __str__(self):
        return self.nome
