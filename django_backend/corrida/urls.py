from django.urls import path
from jogadores.views import salvar_pontuacao, ranking

urlpatterns = [
    path("api/salvar/", salvar_pontuacao),
    path("api/ranking/", ranking),
]
