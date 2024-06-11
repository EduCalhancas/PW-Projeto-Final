from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'festivais'

urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('festival/<int:id>', views.festival_view, name='festival'),
]