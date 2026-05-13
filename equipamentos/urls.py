from django.urls import path

from . import views

urlpatterns = [
    path('', views.lista_equipamentos, name='equipamentos_lista'),
    path('criar/', views.criar_equipamento, name='equipamentos_criar'),
    path('editar/<int:id>/', views.editar_equipamento, name='equipamentos_editar'),
    path('excluir/<int:id>/', views.excluir_equipamento, name='equipamentos_excluir'),
]
