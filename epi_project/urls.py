from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('colaboradores.urls_menu')),
    path('colaboradores/', include('colaboradores.urls')),
    path('equipamentos/', include('equipamentos.urls')),
]