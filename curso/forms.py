from django import forms    # formulários Django
from .models import Curso, AreaCientifica, Disciplina, Projeto, LinguagemProgramacao, Docente

class CursoForm(forms.ModelForm):
  class Meta:
    model = Curso        # classe para a qual é o formulário
    fields = '__all__'   # inclui no form todos os campos da classe Autor.

class AreaCientificaForm(forms.ModelForm):
  class Meta:
    model = AreaCientifica        # classe para a qual é o formulário
    fields = '__all__'   # inclui no form todos os campos da classe Autor.

class DisciplinaForm(forms.ModelForm):
  class Meta:
    model = Disciplina        # classe para a qual é o formulário
    fields = '__all__'   # inclui no form todos os campos da classe Autor.
    widgets = {
      'nome': forms.TextInput(attrs={
          'placeholder':'Nome completo',
      })
    }

class ProjetoForm(forms.ModelForm):
  class Meta:
    model = Projeto        # classe para a qual é o formulário
    fields = '__all__'   # inclui no form todos os campos da classe Autor.

class LinguagemProgramacaoForm(forms.ModelForm):
  class Meta:
    model = LinguagemProgramacao        # classe para a qual é o formulário
    fields = '__all__'   # inclui no form todos os campos da classe Autor.

class DocenteForm(forms.ModelForm):
  class Meta:
    model = Docente        # classe para a qual é o formulário
    fields = '__all__'   # inclui no form todos os campos da classe Autor.