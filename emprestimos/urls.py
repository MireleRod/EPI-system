from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_emprestimos, name='emprestimos_lista'),
    path('criar/', views.criar_emprestimo, name='emprestimos_criar'),
    path('editar/<int:id>/', views.editar_emprestimo, name='emprestimos_editar'),
    path('excluir/<int:id>/', views.excluir_emprestimo, name='emprestimos_excluir'),
]