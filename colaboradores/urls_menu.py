from django.urls import path

from .views_menu import menu_principal

urlpatterns = [
    path('', menu_principal, name='menu_principal'),
]
