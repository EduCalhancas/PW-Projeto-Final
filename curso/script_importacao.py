from django.db import models
import json
from curso.models import Curso, Disciplina

# Carregar dados do JSON
with open('/home/a22204446/project/curso/json/lig.json', 'r') as file:
    data = json.load(file)

# Apagar dados existentes (opcional, depende do requisito)
Curso.objects.all().delete()
Disciplina.objects.all().delete()

# Carregar áreas científicas e disciplinas
for item in data['courseFlatPlan']:
    Disciplina.objects.create(
        curricularIUnitReadableCode=item['curricularIUnitReadableCode'],
        curricularUnitCode=item['curricularUnitCode'],
        nome=item['curricularUnitName'],
        ano=item['curricularYear'],
        semestre=item['semester'],
        ects=item['ects'],
    )
    print(item['curricularUnitName'], item['curricularYear'], item['ects'])  # Exibe informações carregadas

# Carregar informações do curso
curso, created = Curso.objects.get_or_create(
    nome=data['courseDetail']['courseName'],
    apresentacao=data['courseDetail']['competences'],
    objetivos=data['courseDetail']['careerOportunities'],
    competencias=data['courseDetail']['competences']
)


