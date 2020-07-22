from django.urls import path, include
from . import views

urlpatterns = [
    # Formulario para usuario preencher informacoes sobre a passagem
    path('', views.index, name='index'),
    # Mostra as informacoes da passagem que o usuario preencheu
    path('/minha_consulta', views.minha_consulta, name='minha_consulta'),
]
