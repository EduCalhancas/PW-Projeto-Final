from django.shortcuts import get_object_or_404, render
from .models import Banda

# Create your views here.

def index_view(request):
    bandas = Banda.objects.all()
    return render(request, 'bandas/index.html', {'bandas': bandas})

def banda_view(request, idbanda):
    banda = get_object_or_404(Banda, idbanda=idbanda)
    return render(request, 'bandas/banda.html', {'banda': banda})