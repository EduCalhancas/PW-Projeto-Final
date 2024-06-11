from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'curso'

urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('disciplina/<int:curricularUnitCode>', views.disciplina_view, name='disciplina'),
    path('disciplina/nova', views.nova_disciplina_view, name="nova_disciplina"),
    path('disciplina/<int:curricularUnitCode>/edita', views.edita_disciplina_view,name='edita_disciplina'),
    path('disciplina/<int:curricularUnitCode>/apaga', views.apaga_disciplina_view,name="apaga_disciplina"),
    #path('disciplina_projeto/<int:curricularUnitCode>', views.disciplina__projeto_view, name='disciplina_projeto'),
]
