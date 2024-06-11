from django.urls import path
from . import views

app_name = 'bandas'

urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('banda/<int:idbanda>', views.banda_view, name='banda'),
]