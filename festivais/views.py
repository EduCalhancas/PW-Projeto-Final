from django.shortcuts import get_object_or_404, render
from .models import Localizacao, Festival

def index_view(request):
    localizacoes = Localizacao.objects.all()
    context = {

        'localizacoes': localizacoes
    }
    return render(request, 'festivais/index.html', context)


def festival_view(request, id):
    festival = get_object_or_404(Festival, id=id)
    context = {
        'festival': festival
    }
    return render(request, 'festivais/festival.html', context)