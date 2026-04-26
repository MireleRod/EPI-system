from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista, name='lista'),
    path('criar/', views.criar, name='criar'),
    path('editar/<int:id>/', views.editar, name='editar'),
    path('excluir/<int:id>/', views.excluir, name='excluir'),
]