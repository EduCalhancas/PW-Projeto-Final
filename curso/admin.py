from django.contrib import admin
from .models import Curso, AreaCientifica, Disciplina, Projeto, Docente, LinguagemProgramacao

# Register your models here.

admin.site.register(Curso)
admin.site.register(AreaCientifica)
admin.site.register(Disciplina)
admin.site.register(Projeto)
admin.site.register(LinguagemProgramacao)
admin.site.register(Docente)

# Informação útil e maneiras de procurar

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'apresentacao', 'objetivos')
    search_fields = ('nome',)

class AreaCientificaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano', 'semestre', 'ects', 'curricular_unit_code', 'area_cientifica')
    list_filter = ('ano', 'semestre', 'area_cientifica')
    search_fields = ('nome',)

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'disciplina')
    search_fields = ('descricao', 'disciplina__nome')

class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

class LinguagemProgramacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)