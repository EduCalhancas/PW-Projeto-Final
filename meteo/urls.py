from django.urls import path
from . import views  # importamos views para poder usar as suas funções
from .views import ListaCidades, PrevisaoHoje, Previsao5Dias

app_name = 'meteo'

urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('previsao/', views.previsao_view, name='previsao'),
    path('previsao/5-dias/', views.previsao_5_dias_view, name='previsao_5_dias'),
    path('api/cidades/', ListaCidades.as_view(), name='api_cidades'),
    path('api/previsao-hoje/<int:global_id>/', PrevisaoHoje.as_view(), name='api_previsao_hoje'),
    path('api/previsao-5-dias/<int:global_id>/', Previsao5Dias.as_view(), name='api_previsao_5_dias'),
]