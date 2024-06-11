from django.shortcuts import get_object_or_404, render, redirect
from .models import Disciplina
from .forms import DisciplinaForm
from django.contrib.auth.decorators import login_required

#form = AppForm(request.POST or None, request.FILES)

# Create your views here.

def index_view(request):
    disciplinas = Disciplina.objects.all()  # Recupera todas as disciplinas do banco de dados
    return render(request, 'curso/index.html', {'disciplinas': disciplinas})

def disciplina_view(request, curricularUnitCode):
    disciplina = get_object_or_404(Disciplina, curricularUnitCode=curricularUnitCode)
    return render(request, 'curso/disciplina.html', {'disciplina': disciplina})



def nova_disciplina_view(request):

    # criar instância de formulário.
    # Se foram submetidos dados, estes estão em request.POST e o formulario com dados é válido.
    # Senão, o form não tem dados e não é válido
    form = DisciplinaForm(request.POST or None, request.FILES)  # request.FILES deve ser incluido se forem enviados ficheiros ou imagens
    if form.is_valid():
        form.save()
        return redirect('curso:index')

    context = {'form': form}
    return render(request, 'curso/nova_disciplina.html', context)

@login_required
def edita_disciplina_view(request, curricularUnitCode):
    disciplina = get_object_or_404(Disciplina, curricularUnitCode=curricularUnitCode)

    if request.POST:
        form = DisciplinaForm(request.POST or None, request.FILES, instance=disciplina)
        if form.is_valid():
            form.save()
            return redirect('curso:index')
    else:
        form = DisciplinaForm(instance=disciplina)  # cria formulário com dados da instância disciplina

    context = {'form': form, 'disciplina':disciplina}
    return render(request, 'curso/edita_disciplina.html', context)


def apaga_disciplina_view(request, curricularUnitCode):
    disciplina = Disciplina.objects.get(curricularUnitCode=curricularUnitCode)
    disciplina.delete()
    return redirect('curso:index')


